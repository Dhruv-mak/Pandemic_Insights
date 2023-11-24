import React from 'react';
import Plot from 'react-plotly.js';
// import { useState } from 'react';

// TODO: keep this for reference for now
// const unpack = (rows, key) => rows.map(row => row[key]);
// const trace1 = {
//     type: "scatter",
//     mode: "lines",
//     name: 'AAPL High',
//     x: ['2020-01-01', '2020-01-02', '2020-01-04'],
//     y: [86.72, 130.29, 139.41],
//     line: {color: '#17BECF'}
//   };
//   const data = [trace1];

  const LinePlot = ({data}) => {
    const layout = {
      title: 'Time Series with Rangeslider',
      xaxis: {
        autorange: true,
        range: ['2020-01-01', '2020-01-04'],
        rangeselector: {
          buttons: [
            {
              count: 1,
              label: '1m',
              step: 'month',
              stepmode: 'backward'
            },
            {
              count: 6,
              label: '6m',
              step: 'month',
              stepmode: 'backward'
            },
            {step: 'all'}
          ]
        },
        rangeslider: {range: ['2020-01-01', '2020-01-04']},
        type: 'date'
      },
      yaxis: {
        autorange: true,
        range: [86.72, 139.41],
        type: 'linear'
      }
    };
    return (<div>
        <h1>Line Plot</h1>
        <Plot
            data={data}
            layout={layout}
        ></Plot>
    </div>)
}
export default LinePlot;