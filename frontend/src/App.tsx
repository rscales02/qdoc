import React, { useState, useEffect } from 'react';
import './App.css';
import { TRow } from './components/TRow';

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [currentUser, setCurrentUser] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
      setCurrentUser(data.user)
    });
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <p>The current time is {currentTime}.</p>
        <p>The current user is {currentUser}</p>
      </header>
    </div>
  );
}

export default App;
