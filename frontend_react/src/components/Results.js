import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Footer2 from "./Footer2";
import ResultItem from "./ResultItem";
import axios from "axios";

import "./Results.css";

function Results() {
  const [data, setData] = useState([]);

  async function getResults() {
    let names = await axios({
      method: "get",
      url: "http://127.0.0.1:80/result_names",
      headers: {
        "Content-Type": "application/json",
      },
    });

    names = names.data;

    const results = [];

    for (var key in names) {
      const image = await await axios({
        method: "post",
        url: "http://127.0.0.1:80/get_thumbnail",
        data: { filename: names[key]["image_name"] },
        headers: {
          "Content-Type": "application/json",
        },
      });
      results.push({
        title: key,
        image: image.data.image,
      });
    }

    return results;
  }

  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  useEffect(() => {
    const blah = async () => {
      const res = await getResults();
      setData(res);
    };
    blah();

    console.log(data);
  }, []);



  return (
    <>
      <h2 className="heading">Results</h2>
      <div className="gallery-container">


        {data.map((datum) => {
          return <ResultItem props = {datum} key = {datum.title}/>
        })}


        {/* 
        <div className="tile-container">
          <div className="tile-image-container">
            <img className="thumbnail" src="/images/image1.jpg" alt="" />
          </div>
          <div className="tile-title-container">
            <p className="video-title">
              <i class="fa-solid fa-video"></i> Meeting With Peers
            </p>
            <Link className="link" to="/analytics">
              <i class="fa-solid fa-square-poll-vertical"></i> View Results
            </Link>
          </div>
        </div> */}

        {/* <div className="tile-container">
          <div className="tile-image-container">
            <img className="thumbnail" src="/images/image1.jpg" alt="" />
          </div>
          <div className="tile-title-container">
            <p className="video-title">
              <i class="fa-solid fa-video"></i> Meeting With Peers
            </p>
            <Link className="link" to="/analytics">
              <i class="fa-solid fa-square-poll-vertical"></i> View Results
            </Link>
          </div>
        </div> */}

        {/* <div className="tile-container">
          <div className="tile-image-container">
            <img className="thumbnail" src="/images/image1.jpg" alt="" />
          </div>
          <div className="tile-title-container">
            <p className="video-title">
              <i class="fa-solid fa-video"></i> Meeting With Peers
            </p>
            <Link className="link" to="/analytics">
              <i class="fa-solid fa-square-poll-vertical"></i> View Results
            </Link>
          </div>
        </div> */}
      </div>
      <Footer2 />
    </>
  );
}

export default Results;
