import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Home';
import CircuitMaker from './CircuitMaker';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/app" element={<CircuitMaker />} />
      </Routes>
    </Router>
  );
}

export default App;
