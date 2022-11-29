import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Footer2 from "./Footer2";
import axios from "axios";

import "./Results.css";

function ResultItem(props) {
    return (
        <>
        <div className="tile-container">
          <div className="tile-image-container">
            <img className="thumbnail" src = {`data:image/png;base64,${props.props.image}`} alt="" />
          </div>
          <div className="tile-title-container">
            <p className="video-title">
              <i class="fa-solid fa-video"></i> {props.props.title}
            </p>
            <Link className="link" to= {{
                pathname:"/analytics"}}
                state = {props.props.title}>
              <i class="fa-solid fa-square-poll-vertical"></i> View Results
            </Link>
          </div>
        </div>
        </>
    )
}

export default ResultItem;