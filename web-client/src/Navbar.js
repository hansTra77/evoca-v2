import React from 'react'
import FaAngleRight from 'react-icons/lib/fa/angle-right'

import {
  Fixed,
  NavItem,
  Space,
  Toolbar
} from 'rebass'



const Navbar = ({
  config,
  configurations,
  dropdownOpen,
  switchConfig,
  toggle
}) => (
  <Fixed top left right zIndex={1}>
    <Toolbar>
	  <NavItem is="a">
		EVOCA
	  </NavItem>
	  <NavItem is="a">
		<FaAngleRight /> Proyecto Pance
	  </NavItem>
	  <Space
		auto
		x={1}
	  />
	  <NavItem is="a">
		NavItem
	  </NavItem>
	</Toolbar>
  </Fixed>
)

export default Navbar