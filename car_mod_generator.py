#!/usr/bin/env python3
"""
Assetto Corsa Car Mod Generator
Complete tool for creating AC car mods with proper physics and configuration
"""

import os
import json
import math

class ACCarModGenerator:
    def __init__(self, car_name, brand, car_type="fictional"):
        self.car_name = car_name.lower().replace(" ", "_")
        self.display_name = car_name
        self.brand = brand
        self.car_type = car_type
        self.base_path = f"content/cars/{self.car_name}"
        
    def create_directory_structure(self):
        """Create the complete directory structure"""
        dirs = [
            f"{self.base_path}/data",
            f"{self.base_path}/sfx",
            f"{self.base_path}/skins/default",
            f"{self.base_path}/ui"
        ]
        
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
        
        return dirs
    
    def generate_car_ini(self, specs):
        """Generate car.ini file with realistic physics"""
        gear_ratios = specs.get('gear_ratios', [3.5, 2.1, 1.5, 1.2, 1.0, 0.85])
        
        return f"""[INFO]
SCREEN_NAME={self.display_name}
CLASS={specs.get('class', 'street')}
TAGS={','.join(specs.get('tags', ['street']))}
AUTHOR={specs.get('author', 'ModAuthor')}
VERSION=1.0
URL=

[GRAPHICS]
MODEL=car.kn5
COCKPIT_HR=cockpit_HR.kn5
STEER_ANIMATION=steer.ksanim
DRIVER_EYES=0.0,0.75,0.5
DRIVER_EYES_PITCH=0.0

[ENGINE]
POWER_CURVE=engine.lut
COAST_CURVE=coast.lut
TURBO={1 if specs.get('turbo', False) else 0}
LIMITER={specs.get('max_rpm', 8500)}
MINIMUM={specs.get('min_rpm', 1000)}
FUEL_CONSUMPTION={specs.get('fuel_consumption', 1.0)}

[DRIVETRAIN]
TYPE={specs.get('drivetrain', 'RWD')}
GEARS={len(gear_ratios)}
{chr(10).join([f"GEAR_{i+1}={ratio}" for i, ratio in enumerate(gear_ratios)])}
FINAL={specs.get('final_drive', 3.73)}

[TYRES_FRONT]
NAME={specs.get('front_tyre', 'street_245_35_19')}
WIDTH={specs.get('front_width', 245)}
PROFILE={specs.get('front_profile', 35)}
RIM={specs.get('front_rim', 19)}

[TYRES_REAR]
NAME={specs.get('rear_tyre', 'street_295_30_20')}
WIDTH={specs.get('rear_width', 295)}
PROFILE={specs.get('rear_profile', 30)}
RIM={specs.get('rear_rim', 20)}

[AERO]
CD={specs.get('drag_coefficient', 0.32)}
CL_FRONT={specs.get('front_downforce', 0.15)}
CL_REAR={specs.get('rear_downforce', 0.25)}
"""

    def generate_power_curve(self, max_power, max_rpm, power_peak_rpm=None):
        """Generate realistic power curve"""
        if power_peak_rpm is None:
            power_peak_rpm = max_rpm * 0.85
            
        curve = []
        for rpm in range(1000, max_rpm + 500, 500):
            if rpm <= power_peak_rpm:
                # Rising power
                power = max_power * (rpm / power_peak_rpm) * (1 - 0.3 * ((rpm / power_peak_rpm) ** 3))
            else:
                # Falling power after peak
                falloff = (rpm - power_peak_rpm) / (max_rpm - power_peak_rpm)
                power = max_power * (1 - 0.4 * falloff)
            
            curve.append([rpm, max(int(power), 0)])
        
        return curve

    def generate_torque_curve(self, max_torque, max_rpm, torque_peak_rpm=None):
        """Generate realistic torque curve"""
        if torque_peak_rpm is None:
            torque_peak_rpm = max_rpm * 0.6
            
        curve = []
        for rpm in range(1000, max_rpm + 500, 500):
            if rpm <= torque_peak_rpm:
                # Rising torque
                torque = max_torque * (rpm / torque_peak_rpm) * (1.2 - 0.2 * (rpm / torque_peak_rpm))
            else:
                # Falling torque after peak
                falloff = (rpm - torque_peak_rpm) / (max_rpm - torque_peak_rpm)
                torque = max_torque * (1 - 0.5 * falloff)
            
            curve.append([rpm, max(int(torque), 0)])
        
        return curve

    def generate_ui_car_json(self, specs):
        """Generate ui_car.json with calculated curves"""
        power_curve = self.generate_power_curve(
            specs.get('power', 500), 
            specs.get('max_rpm', 8500)
        )
        
        torque_curve = self.generate_torque_curve(
            specs.get('torque', 450), 
            specs.get('max_rpm', 8500)
        )
        
        return {
            "name": self.display_name,
            "brand": self.brand,
            "description": specs.get('description', f"A high-performance {self.car_type} vehicle"),
            "tags": specs.get('tags', ['street']),
            "class": specs.get('class', 'street'),
            "specs": {
                "bhp": str(specs.get('power', 500)),
                "torque": f"{specs.get('torque', 450)} Nm",
                "weight": f"{specs.get('weight', 1400)} kg",
                "topspeed": f"{specs.get('top_speed', 300)} km/h",
                "acceleration": f"0-100: {specs.get('acceleration', 3.5)}s",
                "pwratio": f"{int(specs.get('power', 500) / (specs.get('weight', 1400) / 1000))} bhp/tonne"
            },
            "torqueCurve": torque_curve,
            "powerCurve": power_curve
        }

    def save_mod_files(self, specs, output_dir="./"):
        """Save all mod files to disk"""
        base_dir = os.path.join(output_dir, self.base_path)
        
        # Create directories
        self.create_directory_structure()
        
        # Save car.ini
        car_ini_path = os.path.join(base_dir, "data", "car.ini")
        os.makedirs(os.path.dirname(car_ini_path), exist_ok=True)
        with open(car_ini_path, 'w') as f:
            f.write(self.generate_car_ini(specs))
        
        # Save ui_car.json
        ui_car_path = os.path.join(base_dir, "ui", "ui_car.json")
        os.makedirs(os.path.dirname(ui_car_path), exist_ok=True)
        with open(ui_car_path, 'w') as f:
            json.dump(self.generate_ui_car_json(specs), f, indent=2)
        
        return base_dir

# Predefined car specifications
CAR_SPECS = {
    "fictional_hypercar": {
        'class': 'street',
        'tags': ['street', 'hypercar', 'fictional'],
        'power': 1200,
        'torque': 1100,
        'weight': 1250,
        'max_rpm': 9000,
        'gear_ratios': [3.8, 2.4, 1.8, 1.4, 1.1, 0.9, 0.75, 0.65],
        'drivetrain': 'AWD',
        'turbo': True,
        'drag_coefficient': 0.28,
        'front_downforce': 0.20,
        'rear_downforce': 0.35,
        'description': 'Extreme fictional hypercar with cutting-edge aerodynamics'
    },
    
    "mclaren_p1": {
        'class': 'street',
        'tags': ['street', 'supercar', 'mclaren'],
        'power': 916,
        'torque': 900,
        'weight': 1395,
        'max_rpm': 8500,
        'gear_ratios': [3.5, 2.1, 1.5, 1.2, 1.0, 0.85, 0.7],
        'drivetrain': 'RWD',
        'turbo': True,
        'drag_coefficient': 0.34,
        'front_downforce': 0.15,
        'rear_downforce': 0.30,
        'description': 'Legendary McLaren P1 hybrid hypercar'
    },
    
    "fictional_gt3": {
        'class': 'race',
        'tags': ['race', 'gt3', 'fictional'],
        'power': 550,
        'torque': 650,
        'weight': 1200,
        'max_rpm': 8000,
        'gear_ratios': [3.2, 2.0, 1.5, 1.2, 1.0, 0.85],
        'drivetrain': 'RWD',
        'turbo': False,
        'drag_coefficient': 0.45,
        'front_downforce': 0.40,
        'rear_downforce': 0.80,
        'description': 'Purpose-built GT3 race car with maximum downforce'
    }
}

def main():
    """Generate example car mods"""
    print("=== Assetto Corsa Car Mod Generator ===\n")
    
    cars_to_generate = [
        ("Apex Venom GT", "Apex Dynamics", "fictional_hypercar"),
        ("McLaren P1", "McLaren", "mclaren_p1"),
        ("Thunder R1 GT3", "Thunder Racing", "fictional_gt3")
    ]
    
    for car_name, brand, spec_key in cars_to_generate:
        print(f"Generating: {car_name}")
        generator = ACCarModGenerator(car_name, brand)
        specs = CAR_SPECS[spec_key].copy()
        specs['author'] = 'YourName'
        
        # Generate files
        output_dir = generator.save_mod_files(specs)
        print(f"  Saved to: {output_dir}")
        print(f"  Power: {specs['power']} HP")
        print(f"  Weight: {specs['weight']} kg")
        print()

if __name__ == "__main__":
    main()