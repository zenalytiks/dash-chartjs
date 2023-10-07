import React, {useRef, useState, useEffect} from 'react';
import PropTypes from 'prop-types';

import { Chart as ChartJS, registerables } from 'chart.js';
import { Chart, getElementAtEvent } from 'react-chartjs-2';

import 'chartjs-adapter-moment';
import zoomPlugin from 'chartjs-plugin-zoom';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import annotationPlugin from 'chartjs-plugin-annotation';

ChartJS.register(...registerables,zoomPlugin,ChartDataLabels,annotationPlugin);



/**
 * This component renders ChartJs React component inside Dash App.
 */
export default function ChartJs(props) {
    const { id, setProps, style, type, data, options, toolbox, linearGradientList, linearGradientDirection, useGradient, customCanvasBackgroundColor, clickData } = props;

    const [visibility, setVisibility] = useState('hidden');
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
    const createGradient = (ctx, area, colors) => {
        const isVertical = linearGradientDirection === "vertical";

        const gradient = isVertical
          ? ctx.createLinearGradient(0, area.bottom, 0, area.top)
          : ctx.createLinearGradient(area.left, 0, area.right, 0);   
    


        const step = 1 / (colors.length - 1);
      
        colors.forEach((color, index) => {
          gradient.addColorStop(index * step, color);
        });
      
        return gradient;
    }
    
    const plugins = [];
    
    if (customCanvasBackgroundColor) {
      plugins.push({
        id: 'customCanvasBackgroundColor',
        beforeDraw: (chart, args, options) => {
          const { ctx } = chart;
          ctx.save();
          ctx.globalCompositeOperation = 'destination-over';
          ctx.fillStyle = options.color || customCanvasBackgroundColor;
          ctx.fillRect(0, 0, chart.width, chart.height);
          ctx.restore();
        },
      });
    }
    
    useEffect(() => {
        const chart = chartRef.current;
    
        if (chart && linearGradientList && linearGradientList.length > 0) {

          const chartData = {
            ...data,
            datasets: data.datasets.map((dataset) => {
              const applyBackgroundColor = useGradient === 'backgroundColor' || useGradient === 'both';
              const applyBorderColor = useGradient === 'borderColor' || useGradient === 'both';
    
              return {
                ...dataset,
                backgroundColor: applyBackgroundColor
                  ? createGradient(chart.ctx, chart.chartArea, linearGradientList)
                  : dataset.backgroundColor,
                borderColor: applyBorderColor
                  ? createGradient(chart.ctx, chart.chartArea, linearGradientList)
                  : dataset.borderColor,
              };
            }),
          };
    
          chart.data = chartData;
          chart.update();
        }
    }, [data, linearGradientList, linearGradientDirection, useGradient]);

    
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
                        style={{ background: 'rgba(0,0,0,0)', border: 'none', padding: '0px 5px 0px 5px' }}
                        title='Download'
                        value='print'
                        onClick={downloadChart}
                    >
                        &#11123;
                    </button>

                    <button
                        style={{ background: 'rgba(0,0,0,0)', border: 'none', padding: '0px 5px 0px 5px' }}
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
                data={data}
                options={options}
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
    linearGradientList: [],
    linearGradientDirection: 'vertical',
    useGradient: 'both'
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
     * List of colors for the Linear Gradient.
     */
    linearGradientList: PropTypes.array,

    /**
     * Set the direction of Linear Gradient. Either 'horizontal' or 'vertical'. Vertical is default.
     */
    linearGradientDirection: PropTypes.oneOf(['vertical', 'horizontal']),

    /**
     * Apply Linear Gradient on 'borderColor', 'backgroundColor' or on 'both'. Applies on both by default.
     */
    useGradient: PropTypes.oneOf(['borderColor', 'backgroundColor', 'both']),

    /**
     * Set the Background color of Canvas.
     */
    customCanvasBackgroundColor: PropTypes.string,

    /**
     * clickData returns the datasetIndex and index of data point clicked.
     */
    clickData: PropTypes.object,

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
