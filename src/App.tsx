import React, { useState, useEffect } from 'react';
import './App.css';
import { Card } from './components/Card';

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
            return <Card key={item[0]} name={item[0]} currentPrice={item[1]}></Card>
          })}
          </tbody>
        </table>
      </header>
    </div>
  );
}

export default App;
