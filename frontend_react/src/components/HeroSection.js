import {React, useRef} from 'react';
import '../App.css';
import { Button } from './Button';
import './HeroSection.css';

function HeroSection() {
    const ref = useRef(null);

    const scrollDown = () => {
        window.scrollTo({
            top: document.documentElement.scrollHeight - 1000,
            behavior: "auto",
        });
      };

  return (
    <div className='hero-container'>
      {/* <video src='/videos/video-2.mp4' autoPlay loop muted /> */}
      <img className='video' src='/images/edaa.jpeg' alt = "Main"/>
      <h1>Emotion Detection and Analysis</h1>
      <p>Analyse your digital meetings impact now!</p>
      <div className='hero-btns'>
        <Button
          onClick= {scrollDown}

          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
        >
          GET STARTED
        </Button>
        {/* <Button
          className='btns'
          buttonStyle='btn--primary'
          buttonSize='btn--large'
          onClick={console.log('hey')}
        >
          WATCH TRAILER <i className='far fa-play-circle' />
        </Button> */}
      </div>
    </div>
  );
}

export default HeroSection;