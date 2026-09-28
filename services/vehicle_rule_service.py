from analytics.vehicle_rules import VehicleRuleEngine


class VehicleRuleService:

    def __init__(self, repository):
        self.repository = repository
        self.rule_engine = VehicleRuleEngine()

    def analyze_vehicle(self, vehicle_id: str):

        data = self.repository.get_vehicle(vehicle_id)

        if data.empty:
            raise ValueError(f"Vehicle not found: {vehicle_id}")

        latest = data.iloc[-1]

        result = self.rule_engine.analyze(latest)

        return {
            "vehicle_id": vehicle_id,
            "latest_values": {
                "engine_temperature": float(latest["engine_temperature"]),
                "oil_pressure": float(latest["oil_pressure"]),
                "engine_vibration": float(latest["engine_vibration"]),
                "battery_voltage": float(latest["battery_voltage"]),
                "brake_temperature": float(latest["brake_temperature"])
            },
            **result
        }