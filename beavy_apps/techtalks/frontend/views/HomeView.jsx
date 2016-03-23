import React from 'react'

import homeStyles from '../styles/home.scss'

import { TextCycler } from 'components/TextCycler'

export class HomeView extends React.Component {
  render () {
    const words = ['inspiring', 'amazing']
    return (
      <div className={homeStyles.container}>
        <div className={homeStyles.hero}>
          <h1 className={homeStyles.title}><TextCycler words={words} /> tech talks</h1>
          <p className={homeStyles.claim}>Curated. Voted. Moderated.<br/>
          Only the best videos in Tech.</p>
        </div>
      </div>
    )
  }
}

export default HomeView
