import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { getStoreEntity } from 'utils'

class VideoView extends Component {

  static propTypes = {
    dispatch: PropTypes.func,
    video: PropTypes.object.isRequired
  }

  render () {
    const { video } = this.props

    return <div>
            <span>{video.created_at}</span>
            <h2><a href={video.url} target='_blank'>{video.description}</a></h2>
          </div>
  }
}

function mapStateToProps (state, ownProps) {
  const { videoId } = ownProps.params
  const video = getStoreEntity(state, {id: videoId, type: 'video'})

  return { video }
}

export default connect(
  mapStateToProps
)(VideoView)
