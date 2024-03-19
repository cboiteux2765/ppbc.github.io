import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Tab = createBottomTabNavigator();

const FooterNavigator = () => {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Home"></Tab.Screen>
      <Tab.Screen name="Inventory"></Tab.Screen>
      <Tab.Screen name="Finances"></Tab.Screen>
      <Tab.Screen name="Events"></Tab.Screen>
      <Tab.Screen name="Settings"></Tab.Screen>
    </Tab.Navigator>
  );
}

export default FooterNavigator;