import logo from './logo.svg';
import './App.css';
import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const replacements = [['cool', 'cold'], ['hungry', 'starving'], ['fancy', 'lavish'], ['killed', 'murdered']]
  function handleChange(event) {
    event.preventDefault()
    let data = event.target.value
    replacements.forEach(value => {
      data = data.replace(new RegExp('\\b' + value[0] + '\\b', "g"), value[1]);
      console.log([data, value])
    })
    setText(data)
  }
  return (
    <div className="App">
      <header className="App-header">
        <input value={text} onChange={handleChange}></input>
      </header>
    </div>
  );
}

export default App;
