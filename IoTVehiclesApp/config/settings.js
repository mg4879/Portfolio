/*******************************************************************************
 * Copyright (c) 2014 IBM Corp.
 *
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v1.0 which accompany this distribution.
 *
 * The Eclipse Public License is available at
 *   http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 *   http://www.eclipse.org/org/documents/edl-v10.php.
 *
 * Contributors:
 *   Bryan Boyd - Initial implementation
 *******************************************************************************/

var config = {
	iot_deviceType: "Vehicles",     // replace with your deviceType
	iot_deviceOrg: "4ynuvi",       // replace with your IoT Foundation organization
	iot_deviceSet: [               // replace with your registered device(s)
		{ deviceId: "Vehicle1", token: "_jcvLebtxHUBMzGXo+" },
		{ deviceId: "Vehicle2", token: "PUP*S+W8v_Neq64MOw" },
		{ deviceId: "Vehicle3", token: "OZS(!o3C?D3&TsxT6n" }
	],
	iot_apiKey: "a-4ynuvi-ndlesgae07",    // replace with the key for a generated API token
	iot_apiToken: "N)FN!Q1e2e2vvA!)KB",  // replace with the generated API token

	// these topics will be used by Geospatial Analytics
	notifyTopic: "iot-2/type/api/id/geospatial/cmd/geoAlert/fmt/json",
	inputTopic: "iot-2/type/Vehicles/id/+/evt/telemetry/fmt/json",
};

try {
	module.exports = config;
} catch (e) { window.config = config; }
