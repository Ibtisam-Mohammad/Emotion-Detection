import React from "react";
import "./About.css";
import Footer2 from "../Footer2";
function About() {
  return (
    <>
      <div>
        <h1 className="heading">About</h1>
        {/* <video src='/videos/video-2.mp4' autoPlay loop muted /> */}
        <p className="about">
          EDAA stands for Emotion Detection and Analysis. It is an amazing tool
          that can help you understand the impact of your presentation on your
          audience. If you are new to public speaking or just someone who wants
          to hone this skill, EDAA is the best tool for you. Still think you
          need lengthy feedback forms to understand your audience? Upgrade to
          EDAA, my friend. Gone are the days of long drawn forms that often lack
          credibility. All you need is:<br/><br/>
          <ol>
            <li>A video of your audience with their cameras on.</li>
            <li>
              The audience's consent to be recorded and analyzed anonymously.
            </li>
            <ul>
              <li>
                At EDAA we take consent very seriously. Our tool is designed to
                help the user understand their audience.{" "}
              </li>
              <li>
                It is the moral responsibility of the user to ask their
                audience's consent to be recorded.
              </li>
              <li>
                In case we find that a does not have consent from their
                audience, their account will be suspended.
              </li>
            </ul>
          </ol>
          <br/>
          User Warning: We use a Deep learning model which detects the
          expressions of your audience and predicts a category of emotion that
          best explains facial expressions. We are in no way claiming to
          detect/predict the emotions of a person.<br/> <br/>We are a small group of
          people trying to add value to the on-screen lives of our users. At the
          moment our product is limited to analyzing only web conference-type
          meetings. If you like our product and want to help us build this,
          please contact us at themysticforces007@gmail.com{" "}
        </p>
      </div>
      <Footer2 />
    </>
  );
}

export default About;
