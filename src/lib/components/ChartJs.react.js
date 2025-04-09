import React, {useMemo, useRef, useState, useEffect} from 'react';
import PropTypes from 'prop-types';

import { Chart as ChartJS, registerables } from 'chart.js';
import { Chart, getElementAtEvent } from 'react-chartjs-2';

import 'chartjs-adapter-moment';
import zoomPlugin from 'chartjs-plugin-zoom';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import annotationPlugin from 'chartjs-plugin-annotation';

import { ChoroplethController, GeoFeature, ColorScale, ProjectionScale } from 'chartjs-chart-geo';

ChartJS.register(
    ...registerables,
    zoomPlugin,
    ChartDataLabels,
    annotationPlugin,
    ChoroplethController,
    GeoFeature,
    ColorScale,
    ProjectionScale);



/**
 * This component renders ChartJs React component inside Dash App.
 */
export default function ChartJs(props) {
    const { id, setProps, style, type, data, options, toolbox, customPlugins, clickData, customJSFunctions } = props;

    const [visibility, setVisibility] = useState('hidden');
    const [finalOptions, setFinalOptions] = useState(options);
    const [finalData, setFinalData] = useState(data);
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
    

    const plugins = useMemo(() => {
        const pluginList = [];
    
        if (customPlugins) {
            pluginList.push(...parsePlugins(customPlugins));
        }
    
        return pluginList;
    }, [customPlugins]);    

    
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
                        backgroundColor: 'rgba(0,0,0,0.1)',
                        borderRadius: '5px',
                        float: 'right'
                    }}
                >
                    <button
                        style={{ background: 'rgba(0,0,0,0)', border: 'none', fontSize: '1.2rem' }}
                        title='Download'
                        value='print'
                        onClick={downloadChart}
                    >
                        &#11123;
                    </button>

                    <button
                        style={{ background: 'rgba(0,0,0,0)', border: 'none', fontSize: '1.2rem' }}
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
    customJSFunctions: {},
    customPlugins: {}
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
     * Defines CSS styles which will override styles previously set.
     */
    style: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
