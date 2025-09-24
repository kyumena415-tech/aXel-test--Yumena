import React, { useState } from 'react';

function App() {
  const [result, setResult] = useState(null);

  const fetchData = async () => {
    try {
      const res = await fetch('http://localhost:5000/api/ping');  // ここがAPIのURL
      const data = await res.json();
      setResult(data);
    } catch (error) {
      console.error('API呼び出しエラー:', error);
      setResult({ error: 'API呼び出しに失敗しました' });
    }
  };

  return (
    <div>
      <button onClick={fetchData}>API呼び出し</button>
      <pre>{result ? JSON.stringify(result, null, 2) : '結果がここに表示されます'}</pre>
    </div>
  );
}

export default App;
