import React, { useEffect, useState } from 'react';

function App() {
  const [msg, setMsg] = useState('Loading...');

  useEffect(() => {
    fetch('http://127.0.0.1:5000/ping')
      .then((res) => res.json())
      .then((data) => setMsg(data.message))
      .catch((err) => setMsg('Error: ' + err));
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '2rem' }}>
      <h1>Backend Message:</h1>
      <p>{msg}</p>
    </div>
  );
}

export default App;
