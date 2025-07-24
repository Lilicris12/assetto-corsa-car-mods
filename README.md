# Assetto Corsa Car Mods

Complete templates and tools for creating Assetto Corsa car mods - both real and fictional vehicles with physics tuning guides.

## 🚗 Featured Car Mods

### Fictional Cars
- **Apex Venom GT** - 1200 HP AWD Hypercar
- **Thunder R1 GT3** - 550 HP Race Car

### Real Cars  
- **McLaren P1** - 916 HP Hybrid Hypercar

## 🛠️ Quick Start

1. **Clone this repository**
```bash
git clone https://github.com/Lilicris12/assetto-corsa-car-mods.git
cd assetto-corsa-car-mods
```

2. **Run the generator**
```bash
python car_mod_generator.py
```

3. **Copy to AC directory**
```bash
cp -r content/cars/* "Steam/steamapps/common/assettocorsa/content/cars/"
```

## 📁 Directory Structure

```
content/cars/car_name/
├── data/
│   ├── car.ini          # Main physics configuration
│   ├── engine.ini       # Engine parameters
│   ├── tyres.ini        # Tire physics
│   └── aero.ini         # Aerodynamics
├── sfx/
│   ├── engine.bank      # Engine sounds
│   └── transmission.bank # Gear sounds
├── skins/default/
│   ├── livery.dds       # Car textures
│   └── preview.jpg      # Skin preview
├── ui/
│   ├── ui_car.json      # UI configuration
│   └── badge.png        # Car badge
├── car.kn5              # 3D model
└── collider.kn5         # Collision mesh
```

## 🎯 3D Model Sources

### Real Cars
- **Forza Motorsport/Horizon** - High quality models
- **Gran Turismo** - Detailed interiors
- **Need for Speed** - Street car variants
- **Project CARS** - Race car versions

### Fictional Cars
- **Blender** - Create from scratch
- **3ds Max** - Professional modeling
- **Concept cars** - Real concept designs
- **Kit bashing** - Combine existing parts

## 🔧 Conversion Tools

| Tool | Purpose | Best For |
|------|---------|----------|
| **3DSimED** | Format conversion | Multi-game support |
| **Blender + AC Plugin** | Modeling & export | Custom creations |
| **KsEditor** | Official AC tool | AC-specific features |
| **AC Car Tuner** | Physics tuning | Performance tweaking |

## ⚙️ Physics Tuning Guide

### Aerodynamics
```ini
[AERO]
CD=0.32          # Drag coefficient (0.25-0.35 supercars, 0.4-0.6 race)
CL_FRONT=0.15    # Front downforce (0.1-0.2 road, 0.3-0.5 race)
CL_REAR=0.25     # Rear downforce (0.2-0.4 road, 0.6-1.0 race)
```

### Engine Tuning
```ini
[ENGINE]
LIMITER=8500     # Rev limiter (500-1000 RPM after power peak)
TURBO=1          # Turbo/supercharger (0=NA, 1=forced induction)
```

### Suspension Setup
- **Spring rates**: 20-40 N/mm (road) | 60-120 N/mm (race)
- **Dampers**: 2000-4000 (road) | 6000-12000 (race)  
- **Anti-roll**: 15000-30000 (road) | 50000-100000 (race)

## 🎨 Texture Requirements

### Formats
- **DDS** - Recommended for AC
- **PNG/TGA** - Alternative formats
- **Power-of-2** - 512x512, 1024x1024, 2048x2048

### Maps Needed
- **Diffuse** - Base color/albedo
- **Normal** - Surface detail
- **Specular** - Reflection/roughness
- **Alpha** - Transparency (windows, etc.)

## 📋 Car Specifications

### Fictional Hypercar (Apex Venom GT)
- **Power**: 1200 HP @ 7000 RPM
- **Torque**: 1100 Nm @ 4000 RPM
- **Weight**: 1250 kg
- **Drivetrain**: AWD
- **0-100**: 2.5s
- **Top Speed**: 380 km/h

### Real Car (McLaren P1)
- **Power**: 916 HP (combined)
- **Torque**: 900 Nm
- **Weight**: 1395 kg
- **Drivetrain**: RWD
- **0-100**: 2.8s
- **Top Speed**: 350 km/h

### Race Car (Thunder R1 GT3)
- **Power**: 550 HP @ 7000 RPM
- **Torque**: 650 Nm @ 5000 RPM
- **Weight**: 1200 kg
- **Drivetrain**: RWD
- **Downforce**: High (race spec)

## 🚀 Installation

1. **Extract mod** to AC cars folder:
   ```
   Steam/steamapps/common/assettocorsa/content/cars/
   ```

2. **Required files**:
   - `car.kn5` (3D model)
   - `collider.kn5` (collision)
   - Sound files in `sfx/`
   - Textures in `skins/`

3. **Test in**:
   - Content Manager (recommended)
   - AC Launcher
   - In-game car selection

## 🎮 Testing Checklist

- [ ] Car loads without errors
- [ ] Physics feel realistic
- [ ] Sounds play correctly
- [ ] Textures display properly
- [ ] Performance is balanced
- [ ] AI can drive the car

## 🤝 Contributing

1. Fork the repository
2. Create your car mod
3. Test thoroughly
4. Submit pull request

## 📄 License

This project is open source. Car models may have different licenses - check individual sources.

## 🔗 Useful Links

- [Assetto Corsa Modding Discord](https://discord.gg/acmods)
- [RaceDepartment Forums](https://racedepartment.com)
- [AC Modding Wiki](https://assettocorsa.fandom.com)
- [Content Manager](https://acstuff.ru/app/)

---

**Happy Modding! 🏁**