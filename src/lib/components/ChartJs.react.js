import React, {Component} from 'react';
import PropTypes from 'prop-types';

import { Chart as ChartJS, registerables } from 'chart.js';
import { Chart, getElementAtEvent } from 'react-chartjs-2';

import 'chartjs-adapter-moment';
import zoomPlugin from 'chartjs-plugin-zoom';

ChartJS.register(...registerables,zoomPlugin);



/**
 * This component renders ChartJs React component inside Dash App.
 */
export default class ChartJs extends Component {
    constructor(props) {
        super(props);
        this.chartRef = React.createRef();
      }
    
    render() {
        // eslint-disable-next-line no-unused-vars
        const {id, setProps, style, type, data, options, clickData} = this.props;
        return (
            <div 
                id={id}
                style={style}
            >
                <Chart
                    ref={this.chartRef}
                    type = {type}
                    data = {data}
                    options = {options}
                    onClick = {(event) => {
                        var ele = getElementAtEvent(this.chartRef.current,event)
                        setProps({
                            clickData: {
                                datasetIndex: ele[0].datasetIndex,
                                index: ele[0].index
                            }
                        })
                    }}
                />
                
            </div>
        );
    }
}

ChartJs.defaultProps = {
    data: {
        datasets: []
    },
    options: {},
    clickData: {}
};

ChartJs.propTypes = {

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Chart.js chart type
     */
    type: PropTypes.string,

    /**
     * The data object that is passed into the Chart.js chart
     */
    data: PropTypes.object,

    /**
     * The options object that is passed into the Chart.js chart
     */
    options: PropTypes.object,

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
