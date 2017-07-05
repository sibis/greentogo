import React from 'react';
import {StyleSheet, TextInput, View} from 'react-native';
import {inject, observer} from "mobx-react";
import styles from "../styles";
import { Permissions } from 'expo';
import BarCodeScannerScreen from './BarCodeScannerScreen'

import {
    Container,
    Header,
    Body,
    Title,
    Content,
    Form,
    Item,
    Input,
    Button,
    List,
    ListItem,
    Text,
    Icon,
    Left,
    Right
} from "native-base";
import stylesheet from "../styles";

@inject("appStore")
@observer
class ReturnScreen extends React.Component {
    constructor(props) {
      super(props)
        this.state = {
            hasCameraPermission: false
        }
        this.props.appStore.action = "returnBox";
    }

    static route = {
        navigationBar: {
            title: 'Return container'
        }
    }

    async componentWillMount() {
        const { status } = await Permissions.askAsync(Permissions.CAMERA);
        this.setState({hasCameraPermission: status === 'granted'});
    }

    render() {
        const { hasCameraPermission } = this.state.hasCameraPermission;
        if (hasCameraPermission === null) {
            return <View />;
        } else if (hasCameraPermission === false) {
            return <Text>No access to camera</Text>;
        } else {
            return (
                <View style={{flex: 1}}>
                    <BarCodeScannerScreen />
                </View>
            );
        }
    }
}

export default ReturnScreen;
