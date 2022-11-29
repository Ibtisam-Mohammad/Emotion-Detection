import React from "react";
import "./BarChart.css";
import Plot from "react-plotly.js";
import AnalyticsTable from "./AnalyticsTable";
import Chart1 from "./Chart1";
import Chart2 from "./Chart2";
function BarChart(props) {
  console.log(props);
  return (
    <>
      <div className="plot--container">
        <div className="plot">
          <h2 className="chart-headings">Image Sentiment Analysis</h2>
          <div className="plots">

            <Chart1 props = {props.props}/>
            <Chart2 props = {props.props}/>
            
          </div>
        </div>
        {/* <div className="interpreation">
          <h3>Interpretation</h3>
          <p>
            {" "}
            In the plot on the right, the y axis represents the number of times
            people felt a certain type of emotion. The x axis represents
            emotions divided into 3 categories. Here, positive means emotions
            like happy and suprized and negative means emotions like disgust,sad
            and angry. We have curated these results from the reaction of your
            audiences. More features like Speech Analysis will be added in the
            future, please stay tuned and keep exploring EDAA.
          </p>
        </div> */}

        <div className="speech-analysis">
          <h2 className="chart-headings">Speech Sentiment Analysis</h2>
          {/* <p> In this section we will provide you with a sentimental analysis of your speech
            through out the video. Your speech will be given either positive, negative or neutral. The table below will
            provide you with the sentences and how were they percieved by the audiences in the video.
          </p> */}

          {props.props.table.map((data)=>{
            return <AnalyticsTable props={data}/>
          })}
          {/* <div className="audio-table">
            <h2>Top 5 Highlights- Speech Impact: Neutral</h2>
            <div className="audio-table-headers">
              <h3 className="audio-table-header interval">Interval</h3>
              <h3 className="audio-table-header sentence">Sentence</h3>
              <h3 className="audio-table-header sentiment">
                Predicted Sentiment
              </h3>
              <h3 className="audio-table-header count">Count of People</h3>
            </div>
            <div className="audio-table-items">
              <p className="audio-table-item interval">0-10</p>
              <p className="audio-table-item sentence">
                I do not think this is the best place to talk about such stuff.
              </p>
              <p className="audio-table-item sentiment">Neutral</p>
              <p className="audio-table-item count">40</p>
            </div>
            <div className="audio-table-items">
              <p className="audio-table-item interval">10-20</p>
              <p className="audio-table-item sentence">
                I do not think this is the best place to talk about such stuff.
              </p>
              <p className="audio-table-item sentiment">Neutral</p>
              <p className="audio-table-item count">40</p>
            </div>
          </div>
 */}

          {/* <div className="audio-table">
            <div className="audio-table-headers">
              <h3 className="audio-table-header interval">Interval</h3>
              <h3 className="audio-table-header sentence">Sentence</h3>
              <h3 className="audio-table-header sentiment">
                Predicted Sentiment
              </h3>
              <h3 className="audio-table-header count">Count of People</h3>
            </div>
            <div className="audio-table-items">
              <p className="audio-table-item interval">0-10</p>
              <p className="audio-table-item sentence">
                I do not think this is the best place to talk about such stuff.
              </p>
              <p className="audio-table-item sentiment">Neutral</p>
              <p className="audio-table-item count">40</p>
            </div>
            <div className="audio-table-items">
              <p className="audio-table-item interval">10-20</p>
              <p className="audio-table-item sentence">
                I do not think this is the best place to talk about such stuff.
              </p>
              <p className="audio-table-item sentiment">Neutral</p>
              <p className="audio-table-item count">40</p>
            </div>
          </div> */}


        </div>
      </div>
    </>
  );
}

export default BarChart;
