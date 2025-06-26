import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);

  const handleFileUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("http://localhost:8000/upload/", formData);
    alert("File uploaded: " + res.data.columns.join(", "));
  };

  const handleAsk = async () => {
    const res = await axios.post("http://localhost:8000/ask/", null, {
      params: { query },
    });
    setResponse(res.data);
  };

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">shivaji.ai — Local Data Analyst</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleFileUpload}>Upload CSV</button>

      <input
        className="border p-2 my-4 w-full"
        placeholder="Ask a question about the dataset"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleAsk}>Ask</button>

      {response && (
        <div className="mt-4">
          <h3 className="text-xl font-semibold">Generated Code:</h3>
          <pre className="bg-gray-100 p-4">{response.code}</pre>

          {response.result?.text && (
            <div className="mt-4">
              <h4 className="text-lg font-semibold">Result:</h4>
              <pre>{response.result.text}</pre>
            </div>
          )}

          {response.result?.plot && (
            <div className="mt-4">
              <img src={`data:image/png;base64,${response.result.plot}`} alt="Plot" />
            </div>
          )}

          {response.result?.error && (
            <div className="text-red-600">{response.result.error}</div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
