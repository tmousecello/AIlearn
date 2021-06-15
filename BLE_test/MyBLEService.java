package com.example.iot_ble_test;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;

public class MyBLEService extends Service {
    public MyBLEService() {
    }

    @Override
    public IBinder onBind(Intent intent) {
        // TODO: Return the communication channel to the service.
        throw new UnsupportedOperationException("Not yet implemented");
    }
}
