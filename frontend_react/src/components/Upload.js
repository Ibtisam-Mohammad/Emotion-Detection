import { useEffect, React, useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import "./Upload.css";
import axios from "axios";

function Upload() {
  const [email, setEmail] = useState("");
  const [file, setFile] = useState(null);

  useEffect(() => {}, []);

  const inputFile = useRef(null);

  const handleChange = (e) => {
    setEmail(e.target.value);
  };

  const handleFileChange = (e) => {
    console.log(e.target.files);
    setFile(URL.createObjectURL(e.target.files[0]));
    // setImage(URL.createObjectURL(event.target.files[0]));

    var formData = new FormData();
    formData.append("data", e.target.files[0]);
    axios({
      method: "post",
      url: "http://127.0.0.1:80/video",
      data: formData,
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }).then(function (response) {
      console.log(response);
    });
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!email.endsWith(".com")) {
      alert("Please enter valid email and file");
    } else {
      console.log(email);
      console.log(file);
      setEmail("");
    }
  };
  return (
    <div className="upload--main--container">
      <h1 className="analyzer--heading">Start Analysing</h1>
      <form onSubmit={handleSubmit} className="upload--form">
        <div className="forms--container">
          <label className="input--text">
            <p className="field--heading">Email</p>
            <input
              className="input--box"
              type="text"
              value={email}
              onChange={handleChange}
            />
          </label>
          <label className="input--text">
            <p className="field--heading">Upload Video</p>
            <input
              type="file"
              accept="video/*"
              capture="camera"
              autocomplete="off"
              tabindex="-1"
              reference={inputFile}
              onChange={handleFileChange}
            />
          </label>
          <input
            className="btns btn--primary btn--large"
            type="submit"
            value="Submit"
          />
        </div>
      </form>
    </div>
  );
}

export default Upload;
