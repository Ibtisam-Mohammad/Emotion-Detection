import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import "./pages/Analytics.css";

function AnalyticsTableRows(props){

    return (
        <>
        
        <div className="audio-table-items">
              <p className="audio-table-item interval">{props.props.interval}</p>
              <p className="audio-table-item sentence">{props.props.sentence}</p>
              <p className="audio-table-item sentiment">{props.props.prediction}</p>
              <p className="audio-table-item count">{props.props.people}</p>
            </div>
        
        
        </>
    );



}


export default AnalyticsTableRows;