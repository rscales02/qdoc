import React, { useState, useEffect } from 'react';
import './App.css';
import { TRow } from './components/TRow';

function App() {
  const [cryptoList, setCryptoList] = useState("")
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  useEffect(() => {
    fetch('/get_data').then(res => res.json()).then(data => {
      setCryptoList(data);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>The current time is {currentTime}.</p>
        <table>
          <tbody>
          {Object.entries(cryptoList).map((item) => {
            return <TRow key={item[0]} name={item[0]} value={item[1]}></TRow>
          })}
          </tbody>
        </table>
      </header>
    </div>
  );
}

export default App;
