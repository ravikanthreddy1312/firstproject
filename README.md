import React from 'react';
import './App.css';

import Home from './my-protfolio/Home';
import About from './my-protfolio/About';
import Education from './my-protfolio/Education';
import Skills from './my-protfolio/Skills';
import Projects from './my-protfolio/Projects';
import Contact from './my-protfolio/Contact';
import Footer from './my-protfolio/Footer';

function App() {
  return (
    <div className="App">
      <Home />
      <About />
      <Education />
      <Skills />
      <Projects />
      <Contact />
      <Footer />
    </div>
  );
}

export default App;
