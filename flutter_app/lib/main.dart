import 'package:flutter/material.dart';
import 'package:web_socket_channel/io.dart';
import 'home.dart';

final title = 'WebSocket Demo';

void main () => runApp(
  MaterialApp(
    home: Home(
      channel: IOWebSocketChannel.connect('ws://192.168.0.104:50007'),
      title: title,
    ),
    debugShowCheckedModeBanner: false,
  )
);