import React from 'react';
import { View, Text, Button } from 'react-native';

export default function HomeScreen({ navigation }) {
  return (
    <View>
      <Text>Fumikiri Maze Generator</Text>
      <Button
        title="Start"
        onPress={() => navigation.navigate('Maze')}
      />
    </View>
  );
}
