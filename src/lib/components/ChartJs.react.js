import React, {useMemo, useRef, useState, useEffect} from 'react';
import PropTypes from 'prop-types';

import { Chart as ChartJS, LinearScale, CategoryScale, PointElement, registerables } from 'chart.js';
import { Chart, getElementAtEvent } from 'react-chartjs-2';
import * as Utils from '../Utils';

import 'chartjs-adapter-moment';
import zoomPlugin from 'chartjs-plugin-zoom';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import annotationPlugin from 'chartjs-plugin-annotation';

import { ChoroplethController, BubbleMapController, GeoFeature, ColorScale, ProjectionScale, SizeScale } from 'chartjs-chart-geo';
import { MatrixController, MatrixElement } from 'chartjs-chart-matrix';
import { TreemapController, TreemapElement } from 'chartjs-chart-treemap';
import { BoxPlotController, BoxAndWiskers, ViolinController, Violin } from '@sgratzl/chartjs-chart-boxplot';
import { ForceDirectedGraphController, DendrogramController, TreeController, EdgeLine } from 'chartjs-chart-graph';
import { SankeyController, Flow } from 'chartjs-chart-sankey';
import { ParallelCoordinatesController, LogarithmicParallelCoordinatesController, LinearAxis, LineSegment, PCPScale } from 'chartjs-chart-pcp';

ChartJS.register(
    ...registerables,
    zoomPlugin,
    ChartDataLabels,
    annotationPlugin,
    ChoroplethController,
    BubbleMapController,
    GeoFeature,
    ColorScale,
    ProjectionScale,
    SizeScale,
    MatrixController,
    MatrixElement,
    TreemapController,
    TreemapElement,
    BoxPlotController,
    BoxAndWiskers,
    ViolinController,
    Violin,
    LinearScale,
    CategoryScale,
    ForceDirectedGraphController,
    DendrogramController,
    TreeController,
    EdgeLine,
    PointElement,
    SankeyController,
    Flow,
    ParallelCoordinatesController,
    LogarithmicParallelCoordinatesController,
    PCPScale,
    LineSegment);

ChartJS.registry.addElements(LinearAxis);



/**
 * This component renders ChartJs React component inside Dash App.
 */
export default function ChartJs(props) {
    const { id, setProps, style, type, data, options, redraw, toolbox, customPlugins, clickData, customJSFunctions, actions } = props;

    const [visibility, setVisibility] = useState('hidden');
    const [finalOptions, setFinalOptions] = useState(options);
    const [finalData, setFinalData] = useState(data);
    const [parsedActions, setParsedActions] = useState([]);
    const chartRef = useRef(null);

    const downloadChart = () => {
        const link = document.createElement('a');
        link.download = "chart.png";
        link.href = chartRef.current.toBase64Image('image/png', 1);
        link.click();
    };

    const resetChart = () => {
        chartRef.current.resetZoom('active');
    };

    const handleOnMouseEnter = () => {
        setVisibility('visible');
    };

    const handleOnMouseLeave = () => {
        setVisibility('hidden');
    };

    const injectJSFunctions = (obj, fnMap) => {
        if (!fnMap) return obj;
    
        const deepInject = (target) => {
            if (typeof target === 'object' && target !== null) {
                for (let key in target) {
                    if (typeof target[key] === 'string' && fnMap.hasOwnProperty(target[key])) {
                        try {
                            target[key] = eval(`(${fnMap[target[key]]})`);
                        } catch (e) {
                            console.warn(`Failed to evaluate function for key "${key}"`, e);
                        }
                    } else if (typeof target[key] === 'object') {
                        deepInject(target[key]);
                    }
                }
            }
        };
    
        const newObj = JSON.parse(JSON.stringify(obj));
        deepInject(newObj);
        return newObj;
    };

    // Make Utils available globally for custom functions
    if (typeof window !== 'undefined') {
        window.Utils = Utils;
    }

    // Hook to resize chart on window size changes
    useEffect(() => {
        const handleResize = () => {
            if (chartRef.current) {
                chartRef.current.resize();
            }
        };

        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, []);

    useEffect(() => {
        const processedOptions = injectJSFunctions(options, customJSFunctions);
        setFinalOptions(processedOptions);
    }, [options, customJSFunctions]);

    useEffect(() => {
        const processedData = injectJSFunctions(data, customJSFunctions);
        setFinalData(processedData);

    }, [data,customJSFunctions])


    const parsePlugins = (pluginMap) => {
        const plugins = [];
    
        for (const key in pluginMap) {
            try {
                const pluginObj = eval(`(${pluginMap[key]})`);
                plugins.push(pluginObj);
            } catch (e) {
                console.warn(`Failed to parse plugin "${key}"`, e);
            }
        }
    
        return plugins;
    };

    const parseActions = (actionsList) => {
        if (!actionsList || !Array.isArray(actionsList)) return [];

        return actionsList.map((action) => {
            try {
                return {
                    name: action.name,
                    handler: eval(`(${action.handler})`)
                };
            } catch (e) {
                console.warn(`Failed to parse action "${action.name}"`, e);
                return null;
            }
        }).filter(action => action !== null);
    };
    

    const plugins = useMemo(() => {
        const pluginList = [];
    
        if (customPlugins) {
            pluginList.push(...parsePlugins(customPlugins));
        }
    
        return pluginList;
    }, [customPlugins]);

    useEffect(() => {
        setParsedActions(parseActions(actions));
    }, [actions]);    

    
    return (
        <div
            id={id}
            style={style}
            onMouseEnter={handleOnMouseEnter}
            onMouseLeave={handleOnMouseLeave}
        >
            {toolbox ? (
                <div
                    style={{
                        visibility: visibility,
                        float: 'right'
                    }}
                >
                    <button
                        style={{ backgroundColor: 'rgba(40, 44, 52, .05)', borderColor: 'transparent', fontSize: '1.2rem' }}
                        title='Download'
                        value='print'
                        onClick={downloadChart}
                    >
                        &#11123;
                    </button>

                    <button
                        style={{ backgroundColor: 'rgba(40, 44, 52, .05)', borderColor: 'transparent', fontSize: '1.2rem' }}
                        title='Reset'
                        onClick={resetChart}
                    >
                        &#8634;
                    </button>
                </div>
            ) : null}

            <Chart
                ref={chartRef}
                type={type}
                data={finalData}
                options={finalOptions}
                redraw={redraw}
                plugins={plugins}
                onClick={(event) => {
                    var ele = getElementAtEvent(chartRef.current, event);
                    setProps({
                        clickData: {
                            datasetIndex: ele[0].datasetIndex,
                            index: ele[0].index
                        }
                    });
                }}
            />

            {parsedActions.length > 0 && (
                <div style={{ marginTop: '20px', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
                    {parsedActions.map((action, index) => (
                        <button
                            key={index}
                            onClick={() => action.handler(chartRef.current)}
                            style={{
                                padding: '8px 16px',
                                margin: '0 8px 8px 0',
                                backgroundColor: 'rgba(40, 44, 52, .05)',
                                color: '#3080d0',
                                border: '1px solid transparent',
                                borderRadius: '6px',
                                cursor: 'pointer',
                                fontSize: '0.8rem',
                                display: 'inline-block',
                                textDecoration: 'none',
                                transition: 'background .25s, border-color .25s'
                            }}
                            onMouseOver={(e) => {
                                e.target.style.backgroundColor = 'rgba(48,128,208,.15)';
                                e.target.style.borderColor = 'rgba(48,128,208,.2)';
                            }}
                            onMouseOut={(e) => {
                                e.target.style.backgroundColor = 'rgba(40, 44, 52, .05)';
                                e.target.style.borderColor = 'transparent';
                            }}
                            onMouseDown={(e) => {
                                e.target.style.backgroundColor = 'rgba(48,128,208,.3)';
                                e.target.style.borderColor = 'rgba(48,128,208,.4)';
                            }}
                        >
                            {action.name}
                        </button>
                    ))}
                </div>
            )}
        </div>
    );
};

ChartJs.defaultProps = {
    data: {
        datasets: []
    },
    options: {},
    clickData: {},
    toolbox: true,
    redraw: false,
    customJSFunctions: {},
    customPlugins: {},
    actions: []
};

ChartJs.propTypes = {

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Chart.js chart type.
     */
    type: PropTypes.string,

    /**
     * The data object that is passed into the Chart.js chart.
     */
    data: PropTypes.object,

    /**
     * The options object that is passed into the Chart.js chart.
     */
    options: PropTypes.object,

    /**
     * Teardown and redraw chart on every update.
     */
    redraw: PropTypes.bool,

    /**
     * Toolbox with reset and download buttons for chart.
     */
    toolbox: PropTypes.bool,

    /**
     * clickData returns the datasetIndex and index of data point clicked.
     */
    clickData: PropTypes.object,

    /**
     * Write custom JS functions in dict format.
     */
    customJSFunctions: PropTypes.object,

    /**
     * Write Plugins in dict format.
     */
    customPlugins: PropTypes.object,

    /**
     * List of action objects with name and handler properties.
     * Each action will be rendered as a button below the chart.
     */
    actions: PropTypes.arrayOf(
        PropTypes.shape({
            name: PropTypes.string.isRequired,
            handler: PropTypes.string.isRequired
        })
    ),

    /**
     * Defines CSS styles which will override styles previously set.
     */
    style: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
