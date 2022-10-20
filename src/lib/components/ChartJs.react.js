import React, {Component} from 'react';
import PropTypes from 'prop-types';

import { Chart as ChartJS, registerables } from 'chart.js';
ChartJS.register(...registerables);

import { Chart } from 'react-chartjs-2';
import 'chartjs-adapter-moment';



/**
 * This component renders ChartJs React component inside Dash App.
 */
export default class ChartJs extends Component {
    render() {
        const {id, style, type, data, options} = this.props;

        return (
            <div 
                id={id}
                style={style}
            >
                <Chart
                    type = {type}
                    data = {data}
                    options = {options}
                />
                
            </div>
        );
    }
}

ChartJs.defaultProps = {
    data: {
        datasets: []
    },
    options: {}
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
     * Defines CSS styles which will override styles previously set.
     */
    style: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
