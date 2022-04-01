import React from "react"
import ReactDOM from "react-dom"
import Header from "./Header"
import FoodCard from "./FoodCard"

ReactDOM.render(
    <React.StrictMode>
        <Header />
        <div style={{ position: "relative", paddingTop: "10px" }}>
            <FoodCard />
        </div>
    </React.StrictMode>,
    document.getElementById("root")
)
