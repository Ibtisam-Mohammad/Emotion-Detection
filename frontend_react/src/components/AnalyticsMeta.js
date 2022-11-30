import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Footer2 from "./Footer2";
import "./pages/Analytics.css";
import BarChart from "./BarChart"

function AnalyticsMeta(props) {
    return (
        <>
        <div className="analytics-container">
      <div>
        <h1 className="heading">Analysis Report</h1>
      </div>

      <div className="meta--container">

      <div className="item">
          <span className="metaheaders">Name</span>
          <span className="metavalue">{props.props.filename}</span>
        </div>

        <div className="item">
          <span className="metaheaders">Processed</span>
          <span className="metavalue">True</span>
        </div>

        <div className="item">
          <span className="metaheaders">Clip Interval</span>
          <span className="metavalue">10 secs</span>
        </div>

        <div className="item">
          <span className="metaheaders">User</span>
          <span className="metavalue">themysticforcess007@gmail.com</span>
        </div>

        
      </div>

      <BarChart props={props.props} />

      <Footer2/>
    </div>
        </>
    )
}

export default AnalyticsMeta;