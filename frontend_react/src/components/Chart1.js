import {React, useState, useEffect} from "react";
import "./BarChart.css";
import Plot from "react-plotly.js";
import AnalyticsTable from "./AnalyticsTable";


function Chart1(props){

    const [arr, setArr] = useState([]);
    const [xaxis, setx] = useState([]);

    useEffect(()=>{

        setArr(props.props.chart1);
        setx(['Positive', "Negative", "Neutral"]);



    }, [])

    const transform = () =>{

        let x = [];
        let y = [];
        let plot_data = [];
        let traces = []

        arr.map((integer) => {
            y.push(integer)
        })

        xaxis.map((emotion) => {
            x.push(emotion)
        })

        plot_data['x'] = x;
        plot_data['y'] = y;


        traces.push({
            x: plot_data['x'],
            y: plot_data['y'],
            type: 'bar',
            marker: {color: '#151B54'},
        });

        return traces;






    }

    

    

    console.log(arr)
    return (
        <>
    <Plot
              responisve={true}
              data= {transform()}
              layout={{
                title: "Aggregated Results for the Whole Video",
                xaxis: {
                    title: "Emotion Category",

                  },
                  yaxis: {
                    title: "Count of Reactions",
                  },
              }}
            />
            </>);



}


export default Chart1

