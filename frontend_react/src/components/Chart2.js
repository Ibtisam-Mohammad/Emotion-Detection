import {React, useState, useEffect} from "react";
import "./BarChart.css";
import Plot from "react-plotly.js";
import AnalyticsTable from "./AnalyticsTable";


function Chart2(props){
    console.log(`In Chart2`)
    const [data, setData] = useState([]);

    useEffect(()=>{
        setData(props.props.chart2);
    }, [])

    const transform = ()=> {
        let traces = []
        let color = ['red', 'green', 'blue']
        let names = ['negative', 'positive', 'neutral']
        let i=0

        data.map((datum) =>{
            let plot_data =[]
            plot_data['x'] = datum.x
            plot_data['y'] = datum.y

            traces.push({
                x: plot_data['x'],
                y: plot_data['y'],
                type: 'scatter',
                mode:"lines+markers",
                marker: {color: color[i]},
                name: names[i]
            });
            i+=1;
        })
        return traces
    }


    return(
        <>
        <Plot
        responisve={true}
        data={transform()}
        layout={{
          responisve: true,
          title: "Time Series Impact Analysis",
          xaxis: {
            title: "Time Interval",
            showgrid: false,
            zeroline: false,
          },
          yaxis: {
            title: "Count of Reactions",
            showline: false,
          },
        }}
      />

    </>);
}

export default Chart2