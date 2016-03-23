import React, { PropTypes } from 'react'
import { MainMenu, styles as MenuStyles } from 'components/MainMenu'
import UserModal from 'containers/UserModal'
import UserMenuWidget from 'containers/UserMenuWidget'

import { getExtensions } from 'config/extensions'

import NavigationStyles from './styles/navigation.scss'

const navStyles = Object.assign({}, MenuStyles, NavigationStyles)

export default class Application extends React.Component {
  static propTypes = {
    children: PropTypes.object
  }
  render () {
    return <div>
            <UserModal />
            <MainMenu
              styles={navStyles}
              logo={''}
              name={<span><span className={navStyles.tech}>Tech</span>Talks</span>}
              navigationTools={<UserMenuWidget />} >
              {getExtensions('MainMenuItem').map(x => x.call(this))}
            </MainMenu>
            {this.props.children}
          </div>
  }
}
