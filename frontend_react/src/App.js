
import './App.css';
import Navbar from "./components/Navbar";
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './components/pages/Home';
import About from './components/pages/About';
import Analytics from './components/pages/Analytics';
import Results from './components/Results';
function App() {
  return (
    <>
    <Router>
      <Navbar />
      <Routes>
        <Route path ='/' exact element={<Home/>}/>
        <Route path ='/about' exact element={<About/>} />
        <Route path ='/analytics' exact element={<Analytics props/>} />
        <Route path ='/my_videos' exact element={<Results/>} />
      </Routes>
    </Router>
    </>
  );
}

export default App;
