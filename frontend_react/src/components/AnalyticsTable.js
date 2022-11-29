import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import "./pages/Analytics.css";
import AnalyticsTableRows from "./AnalyticsTableRows";

function AnalyticsTable(props) {

    return (
        <>
         <div className="audio-table">
            <h2>Top Highlights- Speech Impact: {props.props.table}</h2>
            <div className="audio-table-headers">
              <h3 className="audio-table-header interval">Interval</h3>
              <h3 className="audio-table-header sentence">Sentence</h3>
              <h3 className="audio-table-header sentiment">
                Predicted Sentiment
              </h3>
              <h3 className="audio-table-header count">Count of Reactions</h3>
            </div>

            {props.props.rows.map((row)=>{
                return <AnalyticsTableRows props={row}/>
            })}


          </div>
        
        
        
        
        </>


    );




}


export default AnalyticsTable;