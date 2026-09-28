class VehicleRuleEngine:

    def analyze(self, vehicle):
        alerts = []
        risk_points = 0

        engine_temperature = float(vehicle["engine_temperature"])
        oil_pressure = float(vehicle["oil_pressure"])
        engine_vibration = float(vehicle["engine_vibration"])
        battery_voltage = float(vehicle["battery_voltage"])
        brake_temperature = float(vehicle["brake_temperature"])

        if engine_temperature > 110:
            alerts.append({
                "sensor": "engine_temperature",
                "condition": "OVERHEATING",
                "message": "Engine temperature is above the defined overheating threshold."
            })
            risk_points += 3

        if oil_pressure < 2.5:
            alerts.append({
                "sensor": "oil_pressure",
                "condition": "LOW_OIL_PRESSURE",
                "message": "Oil pressure is below the defined threshold."
            })
            risk_points += 3

        if engine_vibration > 3.0:
            alerts.append({
                "sensor": "engine_vibration",
                "condition": "ABNORMAL_VIBRATION",
                "message": "Engine vibration is above the defined threshold."
            })
            risk_points += 2

        if battery_voltage < 13.0:
            alerts.append({
                "sensor": "battery_voltage",
                "condition": "LOW_BATTERY_VOLTAGE",
                "message": "Battery voltage is below the defined running-voltage threshold."
            })
            risk_points += 2

        if brake_temperature > 600:
            alerts.append({
                "sensor": "brake_temperature",
                "condition": "BRAKE_OVERHEATING",
                "message": "Brake temperature is above the defined brake-fade threshold."
            })
            risk_points += 3

        if risk_points >= 6:
            status = "CRITICAL"
        elif risk_points >= 3:
            status = "DEGRADED"
        else:
            status = "HEALTHY"

        return {
            "risk_points": risk_points,
            "status": status,
            "alerts": alerts
        }