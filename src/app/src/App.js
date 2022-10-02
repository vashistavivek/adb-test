import './App.css';
import { useEffect, useState } from 'react'



export function App() {

    const [todos, setTodos] = useState([]);
    const [error, setError] = useState("");

    const getTodos = () => {
        fetch('http://localhost:8000/todos/', { method: 'GET' })
        .then(res => res.json())
        .then(res => {
            setTodos(res.data);
        })
        .catch(err => {
            setError(err.responseJSON);
        });
    }

    const saveTodo = e => {
        e.preventDefault();
        const formData = new FormData(e.target);

        fetch('http://localhost:8000/todos/', { 
        method: 'POST',
        body: formData 
        })
        .then(res => res.json())
        .then(res => {
            getTodos();
            e.target.reset();
        })
        .catch(err => console.error(err));
    }

    useEffect(() => {
        getTodos();
    }, []);

    return (
        <div className="App">
            <div>
                <h1>List of TODOs</h1>
                {
                    todos.length > 0 ?
                        todos.map((todo, index) => (
                            <li key={index}>{todo}</li>
                        )) : 'No todo added yet!'
                }
            </div>
            <div>
                <h1>Create a ToDo</h1>
                <form onSubmit={saveTodo}>
                <div>
                    <label htmlFor="todo">ToDo: </label>
                    <input type="text" name="todo" id="todo"/>
                </div>
                <div style={{"marginTop": "5px"}}>
                    <button type="submit">Add ToDo!</button>
                </div>
                </form>
            </div>
        </div>
    );
}

export default App;
