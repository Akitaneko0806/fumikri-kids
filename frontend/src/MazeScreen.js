import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function MazeScreen() {
  const [maze, setMaze] = useState([]);

  useEffect(() => {
    fetch('http://yourserver.com:5000/generate/15')
      .then(response => response.json())
      .then(data => setMaze(data));
  }, []);

  return (
    <View style={styles.container}>
      {maze.map((row, rowIndex) => (
        <View key={rowIndex} style={styles.row}>
          {row.map((cell, cellIndex) => (
            <View key={cellIndex} style={styles.cell}>
              <Text>{cell}</Text>
            </View>
          ))}
        </View>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
  },
  row: {
    flexDirection: 'row',
  },
  cell: {
    width: 20,
    height: 20,
    borderWidth: 1,
    borderColor: '#000',
  },
});
