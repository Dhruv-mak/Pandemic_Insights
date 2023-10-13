import './App.css';
import React, { useState, useEffect } from 'react';


function App() {
  const [message, setMessage] = useState("")
  useEffect(() => {
    fetch("/api/hello")
      .then(response => {
        if (response.ok){
          return response.json()
        }
        throw new Error("Network response was not ok.")
      })
      .then(response => setMessage(response.message))
      .catch(error => {
        console.error(error)
        setMessage("An error occurred while fetching the API.")
      })
  }, [])
  return (
    <div className="App">
      <h1 className='text-red-700'>{message}</h1>
      </div>
  );
}

export default App;
