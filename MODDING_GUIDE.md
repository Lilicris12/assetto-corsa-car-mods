# Complete Assetto Corsa Car Modding Guide

## 🎯 Overview

This guide covers everything needed to create high-quality car mods for Assetto Corsa, from 3D modeling to physics tuning.

## 📋 Prerequisites

### Software Required
- **3D Modeling**: Blender (free) or 3ds Max
- **AC Tools**: KsEditor, Content Manager
- **Image Editing**: Photoshop, GIMP, or Paint.NET
- **Audio**: Audacity (free)
- **Text Editor**: VS Code, Notepad++

### Skills Needed
- Basic 3D modeling knowledge
- Understanding of car physics
- Texture creation/editing
- File management

## 🚗 Step 1: 3D Model Acquisition

### Option A: Convert Existing Models
```bash
# Common source games:
- Forza Motorsport/Horizon (.fbx, .obj)
- Gran Turismo (.dae, .obj)
- Need for Speed (.nfs, .obj)
- Project CARS (.gmt, .obj)
```

### Option B: Create from Scratch
1. **Reference gathering**: Photos, blueprints, measurements
2. **Base mesh**: Start with basic car shape
3. **Detail modeling**: Add panels, lights, interior
4. **Optimization**: Keep polygon count reasonable (15k-30k)

### Conversion Tools
| Tool | Input Formats | Output | Notes |
|------|---------------|--------|-------|
| 3DSimED | Most game formats | .fbx, .obj | Best for conversions |
| Blender | .fbx, .obj, .dae | .fbx | Free, powerful |
| KsEditor | .fbx | .kn5 | Official AC tool |

## 🔧 Step 2: Model Preparation

### Mesh Requirements
- **Clean topology**: No overlapping faces
- **Proper normals**: All facing outward
- **UV mapping**: Non-overlapping, efficient layout
- **Pivot point**: At ground level, car center

### Essential Components
```
car_body          # Main body mesh
wheels_front_L/R  # Front wheels
wheels_rear_L/R   # Rear wheels
interior          # Cockpit/dashboard
glass            # Windows (separate for transparency)
lights_front     # Headlights
lights_rear      # Taillights
```

### LOD (Level of Detail)
- **LOD_A**: Full detail (player view)
- **LOD_B**: Medium detail (close AI cars)
- **LOD_C**: Low detail (distant cars)

## 🎨 Step 3: Texturing

### Texture Maps Needed
1. **Diffuse**: Base color/albedo
2. **Normal**: Surface detail and bumps
3. **Specular**: Reflection intensity
4. **Alpha**: Transparency (windows, grilles)

### Resolution Guidelines
- **Body panels**: 2048x2048 or 1024x1024
- **Interior**: 1024x1024
- **Wheels**: 512x512
- **Details**: 256x256 or 512x512

### Format Requirements
```ini
# Recommended formats:
Primary: .dds (best performance)
Alternative: .png, .tga
Compression: DXT1 (no alpha), DXT5 (with alpha)
```

## ⚙️ Step 4: Physics Configuration

### car.ini Structure
```ini
[INFO]           # Basic car information
[GRAPHICS]       # 3D model references
[ENGINE]         # Power, torque, RPM limits
[DRIVETRAIN]     # Gears, differential
[TYRES_FRONT]    # Front tire specifications
[TYRES_REAR]     # Rear tire specifications
[AERO]           # Aerodynamics
[SUSPENSION]     # Springs, dampers
[BRAKES]         # Braking force
```

### Engine Tuning
```ini
[ENGINE]
POWER_CURVE=engine.lut    # Power vs RPM curve
COAST_CURVE=coast.lut     # Engine braking
TURBO=1                   # 0=NA, 1=Turbo/Super
LIMITER=8500             # Rev limiter RPM
MINIMUM=1000             # Idle RPM
FUEL_CONSUMPTION=1.0     # Fuel usage multiplier
```

### Realistic Power Curves
- **Peak power**: Usually 500-1000 RPM before redline
- **Peak torque**: Typically 2000-3000 RPM before peak power
- **Curve shape**: Smooth, realistic progression

### Aerodynamics Tuning
```ini
[AERO]
CD=0.32          # Drag coefficient
CL_FRONT=0.15    # Front downforce
CL_REAR=0.25     # Rear downforce

# Realistic values:
# Road cars: CD=0.25-0.35, CL=0.1-0.3
# Race cars: CD=0.4-0.6, CL=0.5-1.2
```

## 🔊 Step 5: Sound Implementation

### Required Sound Files
```
sfx/
├── engine.bank          # Engine sounds
├── transmission.bank    # Gear changes
├── surfaces.bank        # Tire/road interaction
└── wind.bank           # Wind noise
```

### Sound Sources
1. **Record real car**: Best authenticity
2. **Extract from games**: Forza, GT, etc.
3. **Synthesize**: Using audio tools
4. **Community banks**: Shared sound packs

### Audio Processing
- **Format**: .wav, 44.1kHz, 16-bit
- **Length**: 2-10 seconds per sample
- **Looping**: Seamless for engine sounds
- **Volume**: Consistent levels

## 🎮 Step 6: Testing & Tuning

### Initial Testing
1. **Load test**: Car appears in game
2. **Physics check**: Realistic handling
3. **Visual check**: Textures, lighting
4. **Audio check**: Sounds play correctly

### Performance Tuning
```ini
# Lap time targets (Spa-Francorchamps):
Street cars: 2:30-2:50
Supercars: 2:15-2:30
GT3 cars: 2:15-2:25
F1 cars: 1:40-1:50
```

### Common Issues & Fixes
| Problem | Cause | Solution |
|---------|-------|----------|
| Car won't load | Missing .kn5 | Check file paths |
| No sound | Missing .bank files | Add sound files |
| Poor handling | Bad suspension setup | Adjust spring/damper rates |
| Too fast/slow | Wrong power/weight | Adjust engine.lut |

## 📦 Step 7: Packaging & Distribution

### File Structure Check
```
content/cars/your_car/
├── data/
│   ├── car.ini ✓
│   ├── engine.ini ✓
│   └── tyres.ini ✓
├── sfx/
│   └── engine.bank ✓
├── skins/default/
│   ├── livery.dds ✓
│   └── preview.jpg ✓
├── ui/
│   ├── ui_car.json ✓
│   └── badge.png ✓
├── car.kn5 ✓
└── collider.kn5 ✓
```

### Quality Checklist
- [ ] Car loads without errors
- [ ] Realistic performance
- [ ] Good visual quality
- [ ] Proper sounds
- [ ] AI compatibility
- [ ] Multiplayer tested

### Distribution Platforms
- **RaceDepartment**: Most popular
- **AssettoLand**: Alternative platform
- **GitHub**: Open source projects
- **Discord**: Community sharing

## 🔧 Advanced Techniques

### Custom Shaders
- **ksPerPixel**: Standard car shader
- **ksPerPixelMultiMap**: Multiple texture maps
- **ksWindscreen**: Glass materials
- **ksTyres**: Tire-specific shader

### Animation Setup
```ini
# Steering wheel animation
STEER_ANIMATION=steer.ksanim
STEER_LOCK=450    # Degrees of rotation

# Suspension animation
SUSP_TRAVEL=0.15  # Meters of travel
```

### Data Analysis
- **Telemetry**: Use AC telemetry apps
- **Comparison**: Test against similar cars
- **Community feedback**: Beta testing

## 📚 Resources

### Learning Materials
- [AC Modding Discord](https://discord.gg/acmods)
- [RaceDepartment Tutorials](https://racedepartment.com)
- [YouTube Modding Channels](https://youtube.com)

### Tools Download
- [Content Manager](https://acstuff.ru/app/)
- [KsEditor](https://assettocorsa.net/forum/)
- [3DSimED](https://sim-garage.co.uk/)

### Reference Data
- [Real car specifications](https://fastestlaps.com)
- [Physics references](https://en.wikipedia.org/wiki/Vehicle_dynamics)
- [Tire data](https://tirerack.com)

## 🎯 Pro Tips

1. **Start simple**: Begin with existing car modifications
2. **Reference real data**: Use actual car specifications
3. **Test frequently**: Small iterations work better
4. **Community feedback**: Share WIP for input
5. **Document everything**: Keep notes on changes
6. **Backup often**: Version control your work

---

**Happy modding! 🏁**