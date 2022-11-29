import React from 'react';
import '../../App.css';
import Upload from '../Upload';
import HeroSection from '../HeroSection';
import Footer from '../Footer';
import Results from '../Results';
import Analytics from './Analytics';

function Home() {
  return (
    <>
      <HeroSection />
      <Upload />
      {/* <Analytics /> */}
      <Footer />
    </>
  );
}

export default Home;