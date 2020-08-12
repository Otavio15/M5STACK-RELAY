import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:web_socket_channel/io.dart';
import 'package:web_socket_channel/status.dart';
import 'package:web_socket_channel/web_socket_channel.dart';


class Home extends StatefulWidget {

  final String title;
  final WebSocketChannel channel;

  Home({Key key, @required this.title, @required this.channel})
      : super(key: key);

  @override
  _HomeState createState() => _HomeState();
}


class _HomeState extends State<Home> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.all(32),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Image.asset("imagens/tecpy.png"),
              Padding(
                padding: EdgeInsets.only(top: 50, bottom: 50),
                child: Column(
                  children: [
                    Padding(
                      padding: EdgeInsets.only(bottom: 20),
                      child: RaisedButton(
                        onPressed: _sendMessageA,
                        color: Colors.red,
                        padding: EdgeInsets.only(left: 70, right: 70),
                        child: Icon(
                          Icons.keyboard_arrow_up,
                          color: Colors.white,
                          size: 50,
                        ),
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.only(bottom: 20),
                      child: RaisedButton(
                        onPressed: _sendMessageB,
                        color: Colors.red,
                        padding: EdgeInsets.only(left: 70, right: 70),
                        child: Icon(
                          Icons.stop,
                          color: Colors.white,
                          size: 50,
                        ),
                      ),
                    ),
                    RaisedButton(
                      onPressed: _sendMessageC,
                      color: Colors.red,
                      padding: EdgeInsets.only(left: 70, right: 70),
                      child: Icon(
                        Icons.keyboard_arrow_down,
                        color: Colors.white,
                        size: 50,
                      ),
                    ),
                    StreamBuilder(
                      stream: widget.channel.stream,
                      builder: (context, snapshot) {
                        return Padding(
                          padding: const EdgeInsets.symmetric(vertical: 24.0),
                          child: Text(snapshot.hasData ? '${snapshot.data}' : ''),
                        );
                      },
                    )
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }

  void _sendMessageA() {
    widget.channel.sink.add("a");
  }

  void _sendMessageB() {
    widget.channel.sink.add("b");
  }

  void _sendMessageC() {
    widget.channel.sink.add("c");
  }

  @override
  void dispose() {
    widget.channel.sink.close();
    super.dispose();
  }

}
