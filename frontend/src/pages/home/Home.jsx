import { useState } from 'react'
//import Header from "../../components/header/Header.jsx"
import MainButton from "@buttons/main_button/MainButton.jsx"
import {BUTTON_TEXT} from "../../constants.js"

function Home() {
  const [count, setCount] = useState(0)

  return (
    <>
        <section className="title-section">
            <h1>CollTaskTracker</h1>
            <div className="title-buttons">
                <MainButton key={1} text_button={BUTTON_TEXT.signIn}/>
                <MainButton key={2}  text_button={BUTTON_TEXT.signUp}/>
            </div>

        </section>
    </>
  )
}

export default Home
