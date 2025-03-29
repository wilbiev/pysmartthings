"""Capability model."""

from enum import StrEnum


class Capability(StrEnum):
    """Capability model."""

    ACCELERATION_SENSOR = "accelerationSensor"
    ACTIVITY_LIGHTING_MODE = "activityLightingMode"
    ACTIVITY_SENSOR = "activitySensor"
    AIR_CONDITIONER_FAN_MODE = "airConditionerFanMode"
    AIR_CONDITIONER_MODE = "airConditionerMode"
    AIR_PURIFIER_FAN_MODE = "airPurifierFanMode"
    AIR_QUALITY_HEALTH_CONCERN = "airQualityHealthConcern"
    AIR_QUALITY_SENSOR = "airQualitySensor"
    ALARM = "alarm"
    ATMOSPHERIC_PRESSURE_MEASUREMENT = "atmosphericPressureMeasurement"
    AUDIO_MUTE = "audioMute"
    AUDIO_NOTIFICATION = "audioNotification"
    AUDIO_STREAM = "audioStream"
    AUDIO_TRACK_ADDRESSING = "audioTrackAddressing"
    AUDIO_TRACK_DATA = "audioTrackData"
    AUDIO_VOLUME = "audioVolume"
    BATTERY = "battery"
    BATTERY_LEVEL = "batteryLevel"
    BODY_MASS_INDEX_MEASUREMENT = "bodyMassIndexMeasurement"
    BODY_WEIGHT_MEASUREMENT = "bodyWeightMeasurement"
    BRIDGE = "bridge"
    BUTTON = "button"
    BYPASSABLE = "bypassable"
    CARBON_DIOXIDE_HEALTH_CONCERN = "carbonDioxideHealthConcern"
    CARBON_DIOXIDE_MEASUREMENT = "carbonDioxideMeasurement"
    CARBON_MONOXIDE_DETECTOR = "carbonMonoxideDetector"
    CARBON_MONOXIDE_MEASUREMENT = "carbonMonoxideMeasurement"
    CHIME = "chime"
    COLOR_CONTROL = "colorControl"
    COLOR_TEMPERATURE = "colorTemperature"
    CONFIGURATION = "configuration"
    CONTACT_SENSOR = "contactSensor"
    CURRENT_MEASUREMENT = "currentMeasurement"
    DEMAND_RESPONSE_LOAD_CONTROL = "demandResponseLoadControl"
    DEW_POINT = "dewPoint"
    DISHWASHER_OPERATING_STATE = "dishwasherOperatingState"
    DOOR_CONTROL = "doorControl"
    DRYER_MODE = "dryerMode"
    DRYER_OPERATING_STATE = "dryerOperatingState"
    DUST_HEALTH_CONCERN = "dustHealthConcern"
    DUST_SENSOR = "dustSensor"
    ELEVATOR_CALL = "elevatorCall"
    ENERGY_METER = "energyMeter"
    EQUIVALENT_CARBON_DIOXIDE_MEASUREMENT = "equivalentCarbonDioxideMeasurement"
    EXECUTE = "execute"
    FAN_OSCILLATION_MODE = "fanOscillationMode"
    FAN_SPEED = "fanSpeed"
    FAN_SPEED_PERCENT = "fanSpeedPercent"
    FILTER_STATE = "filterState"
    FILTER_STATUS = "filterStatus"
    FINE_DUST_HEALTH_CONCERN = "fineDustHealthConcern"
    FINE_DUST_SENSOR = "fineDustSensor"
    FIRMWARE_UPDATE = "firmwareUpdate"
    FORMALDEHYDE_HEALTH_CONCERN = "formaldehydeHealthConcern"
    FORMALDEHYDE_MEASUREMENT = "formaldehydeMeasurement"
    GAS_DETECTOR = "gasDetector"
    GAS_METER = "gasMeter"
    GEOFENCE = "geofence"
    GEOLOCATION = "geolocation"
    HARDWARE_FAULT = "hardwareFault"
    HEALTH_CHECK = "healthCheck"
    HUMIDIFIER_MODE = "humidifierMode"
    ILLUMINANCE_MEASUREMENT = "illuminanceMeasurement"
    IMAGE_CAPTURE = "imageCapture"
    INFRARED_LEVEL = "infraredLevel"
    KEYPAD_INPUT = "keypadInput"
    LAUNDRY_WASHER_RINSE_MODE = "laundryWasherRinseMode"
    LAUNDRY_WASHER_SPIN_SPEED = "laundryWasherSpinSpeed"
    LOCK = "lock"
    LOCK_CODES = "lockCodes"
    LOG_TRIGGER = "logTrigger"
    MEDIA_GROUP = "mediaGroup"
    MEDIA_INPUT_SOURCE = "mediaInputSource"
    MEDIA_PLAYBACK = "mediaPlayback"
    MEDIA_PLAYBACK_REPEAT = "mediaPlaybackRepeat"
    MEDIA_PLAYBACK_SHUFFLE = "mediaPlaybackShuffle"
    MEDIA_PRESETS = "mediaPresets"
    MEDIA_TRACK_CONTROL = "mediaTrackControl"
    MODE = "mode"
    MOLD_HEALTH_CONCERN = "moldHealthConcern"
    MOMENTARY = "momentary"
    MOTION_SENSOR = "motionSensor"
    MUSIC_PLAYER = "musicPlayer"
    NETWORK_METER = "networkMeter"
    NITROGEN_DIOXIDE_HEALTH_CONCERN = "nitrogenDioxideHealthConcern"
    NITROGEN_DIOXIDE_MEASUREMENT = "nitrogenDioxideMeasurement"
    NOTIFICATION = "notification"
    OBJECT_DETECTION = "objectDetection"
    OCCUPANCY_SENSOR = "occupancySensor"
    OCF = "ocf"
    ODOR_SENSOR = "odorSensor"
    OVEN_MODE = "ovenMode"
    OVEN_OPERATING_STATE = "ovenOperatingState"
    OVEN_SETPOINT = "ovenSetpoint"
    OZONE_HEALTH_CONCERN = "ozoneHealthConcern"
    OZONE_MEASUREMENT = "ozoneMeasurement"
    PH_MEASUREMENT = "pHMeasurement"
    PANIC_ALARM = "panicAlarm"
    PEST_CONTROL = "pestControl"
    POWER_CONSUMPTION_REPORT = "powerConsumptionReport"
    POWER_METER = "powerMeter"
    POWER_SOURCE = "powerSource"
    PRECIPITATION_SENSOR = "precipitationSensor"
    PRESENCE_SENSOR = "presenceSensor"
    RADON_MEASUREMENT = "radonMeasurement"
    REFRESH = "refresh"
    REFRIGERATION = "refrigeration"
    REFRIGERATION_SETPOINT = "refrigerationSetpoint"
    RELATIVE_BRIGHTNESS = "relativeBrightness"
    RELATIVE_HUMIDITY_MEASUREMENT = "relativeHumidityMeasurement"
    REMOTE_CONTROL_STATUS = "remoteControlStatus"
    RICE_COOKER = "riceCooker"
    ROBOT_CLEANER_CLEANING_MODE = "robotCleanerCleaningMode"
    ROBOT_CLEANER_MOVEMENT = "robotCleanerMovement"
    ROBOT_CLEANER_OPERATING_STATE = "robotCleanerOperatingState"
    ROBOT_CLEANER_TURBO_MODE = "robotCleanerTurboMode"
    SECURITY_SYSTEM = "securitySystem"
    SIGNAL_STRENGTH = "signalStrength"
    SLEEP_SENSOR = "sleepSensor"
    SMOKE_DETECTOR = "smokeDetector"
    SOUND_DETECTION = "soundDetection"
    SOUND_PRESSURE_LEVEL = "soundPressureLevel"
    SOUND_SENSOR = "soundSensor"
    SPEECH_SYNTHESIS = "speechSynthesis"
    STATELESS_CUSTOM_BUTTON = "statelessCustomButton"
    STATELESS_FANSPEED_BUTTON = "statelessFanspeedButton"
    STATELESS_POWER_TOGGLE_BUTTON = "statelessPowerToggleButton"
    SWITCH = "switch"
    SWITCH_LEVEL = "switchLevel"
    T_V = "tV"
    TAMPER_ALERT = "tamperAlert"
    TEMPERATURE_ALARM = "temperatureAlarm"
    TEMPERATURE_LEVEL = "temperatureLevel"
    TEMPERATURE_MEASUREMENT = "temperatureMeasurement"
    TEMPERATURE_SETPOINT = "temperatureSetpoint"
    THERMOSTAT_COOLING_SETPOINT = "thermostatCoolingSetpoint"
    THERMOSTAT_FAN_MODE = "thermostatFanMode"
    THERMOSTAT_HEATING_SETPOINT = "thermostatHeatingSetpoint"
    THERMOSTAT_MODE = "thermostatMode"
    THERMOSTAT_OPERATING_STATE = "thermostatOperatingState"
    THERMOSTAT_SETPOINT = "thermostatSetpoint"
    THREE_AXIS = "threeAxis"
    TONE = "tone"
    TV_CHANNEL = "tvChannel"
    TVOC_MEASUREMENT = "tvocMeasurement"
    ULTRAVIOLET_INDEX = "ultravioletIndex"
    VALVE = "valve"
    VERY_FINE_DUST_HEALTH_CONCERN = "veryFineDustHealthConcern"
    VERY_FINE_DUST_SENSOR = "veryFineDustSensor"
    VIDEO_CAMERA = "videoCamera"
    VIDEO_CAPTURE = "videoCapture"
    VIDEO_STREAM = "videoStream"
    VOLTAGE_MEASUREMENT = "voltageMeasurement"
    WASHER_MODE = "washerMode"
    WASHER_OPERATING_STATE = "washerOperatingState"
    WATER_SENSOR = "waterSensor"
    WEBRTC = "webrtc"
    WIND_MODE = "windMode"
    WINDOW_SHADE = "windowShade"
    WINDOW_SHADE_LEVEL = "windowShadeLevel"
    WINDOW_SHADE_PRESET = "windowShadePreset"
    ZWAVE_MULTICHANNEL = "zwMultichannel"

    CUSTOM_ACCESSIBILITY = "custom.accessibility"
    CUSTOM_AIR_CONDITIONER_ODOR_CONTROLLER = "custom.airConditionerOdorController"
    CUSTOM_AIR_CONDITIONER_OPTIONAL_MODE = "custom.airConditionerOptionalMode"
    CUSTOM_AIR_CONDITIONER_TROPICAL_NIGHT_MODE = (
        "custom.airConditionerTropicalNightMode"
    )
    CUSTOM_AIR_PURIFIER_OPERATION_MODE = "custom.airPurifierOperationMode"
    CUSTOM_AIR_QUALITY_MAX_LEVEL = "custom.airQualityMaxLevel"
    CUSTOM_AUTO_CLEANING_MODE = "custom.autoCleaningMode"
    CUSTOM_COOKTOP_OPERATING_STATE = "custom.cooktopOperatingState"
    CUSTOM_DEODOR_FILTER = "custom.deodorFilter"
    CUSTOM_DEVICE_DEPENDENCY_STATUS = "custom.deviceDependencyStatus"
    CUSTOM_DEVICE_REPORT_STATE_CONFIGURATION = "custom.deviceReportStateConfiguration"
    CUSTOM_DISABLED_CAPABILITIES = "custom.disabledCapabilities"
    CUSTOM_DISABLED_COMPONENTS = "custom.disabledComponents"
    CUSTOM_DISHWASHER_DELAY_START_TIME = "custom.dishwasherDelayStartTime"
    CUSTOM_DISHWASHER_OPERATING_PERCENTAGE = "custom.dishwasherOperatingPercentage"
    CUSTOM_DISHWASHER_OPERATING_PROGRESS = "custom.dishwasherOperatingProgress"
    CUSTOM_DO_NOT_DISTURB_MODE = "custom.doNotDisturbMode"
    CUSTOM_DRYER_DRY_LEVEL = "custom.dryerDryLevel"
    CUSTOM_DRYER_WRINKLE_PREVENT = "custom.dryerWrinklePrevent"
    CUSTOM_DUST_FILTER = "custom.dustFilter"
    CUSTOM_ELECTRIC_HEPA_FILTER = "custom.electricHepaFilter"
    CUSTOM_ENERGY_TYPE = "custom.energyType"
    CUSTOM_ERROR = "custom.error"
    CUSTOM_FILTER_USAGE_TIME = "custom.filterUsageTime"
    CUSTOM_FRIDGE_MODE = "custom.fridgeMode"
    CUSTOM_HEPA_FILTER = "custom.hepaFilter"
    CUSTOM_JOB_BEGINNING_STATUS = "custom.jobBeginningStatus"
    CUSTOM_LAUNCH_APP = "custom.launchapp"
    CUSTOM_LOWER_DEVICE_POWER = "custom.lowerDevicePower"
    CUSTOM_OCF_RESOURCE_VERSION = "custom.ocfResourceVersion"
    CUSTOM_OUTING_MODE = "custom.outingMode"
    CUSTOM_OVEN_CAVITY_STATUS = "custom.ovenCavityStatus"
    CUSTOM_PERIODIC_SENSING = "custom.periodicSensing"
    CUSTOM_PICTURE_MODE = "custom.picturemode"
    CUSTOM_RECORDING = "custom.recording"
    CUSTOM_SOUND_MODE = "custom.soundmode"
    CUSTOM_SPI_MODE = "custom.spiMode"
    CUSTOM_STEAM_CLOSET_OPERATING_STATE = "custom.steamClosetOperatingState"
    CUSTOM_STEAM_CLOSET_WRINKLE_PREVENT = "custom.steamClosetWrinklePrevent"
    CUSTOM_SUPPORTED_OPTIONS = "custom.supportedOptions"
    CUSTOM_THERMOSTAT_SETPOINT_CONTROL = "custom.thermostatSetpointControl"
    CUSTOM_TV_SEARCH = "custom.tvsearch"
    CUSTOM_USER_NOTIFICATION = "custom.userNotification"
    CUSTOM_VERY_FINE_DUST_FILTER = "custom.veryFineDustFilter"
    CUSTOM_VIRUS_DOCTOR_MODE = "custom.virusDoctorMode"
    CUSTOM_WASHER_AUTO_DETERGENT = "custom.washerAutoDetergent"
    CUSTOM_WASHER_AUTO_SOFTENER = "custom.washerAutoSoftener"
    CUSTOM_WASHER_RINSE_CYCLES = "custom.washerRinseCycles"
    CUSTOM_WASHER_SOIL_LEVEL = "custom.washerSoilLevel"
    CUSTOM_WASHER_SPIN_LEVEL = "custom.washerSpinLevel"
    CUSTOM_WASHER_WATER_TEMPERATURE = "custom.washerWaterTemperature"
    CUSTOM_WATER_FILTER = "custom.waterFilter"
    CUSTOM_WELCOME_CARE_MODE = "custom.welcomeCareMode"

    SAMSUNG_CE_AIR_CONDITIONER_AUDIO_FEEDBACK = "samsungce.airConditionerAudioFeedback"
    SAMSUNG_CE_AIR_CONDITIONER_BEEP = "samsungce.airConditionerBeep"
    SAMSUNG_CE_AIR_CONDITIONER_DISPLAY = "samsungce.airConditionerDisplay"
    SAMSUNG_CE_AIR_CONDITIONER_LIGHTING = "samsungce.airConditionerLighting"
    SAMSUNG_CE_AIR_QUALITY_HEALTH_CONCERN = "samsungce.airQualityHealthConcern"
    SAMSUNG_CE_ALWAYS_ON_SENSING = "samsungce.alwaysOnSensing"
    SAMSUNG_CE_AUTO_DISPENSE_DETERGENT = "samsungce.autoDispenseDetergent"
    SAMSUNG_CE_AUTO_DISPENSE_SOFTENER = "samsungce.autoDispenseSoftener"
    SAMSUNG_CE_AUTO_DOOR_RELEASE = "samsungce.autoDoorRelease"
    SAMSUNG_CE_AUTO_VENTILATION = "samsungce.autoVentilation"
    SAMSUNG_CE_BUTTON_DISPLAY_CONDITION = "samsungce.buttonDisplayCondition"
    SAMSUNG_CE_CAMERA_STREAMING = "samsungce.cameraStreaming"
    SAMSUNG_CE_CLOTHING_EXTRA_CARE = "samsungce.clothingExtraCare"
    SAMSUNG_CE_CONNECTION_STATE = "samsungce.connectionState"
    SAMSUNG_CE_CONSUMED_ENERGY = "samsungce.consumedEnergy"
    SAMSUNG_CE_COOK_RECIPE = "samsungce.cookRecipe"
    SAMSUNG_CE_COOKTOP_BURNER_MODE = "samsungce.cooktopBurnerMode"
    SAMSUNG_CE_COOKTOP_HEATING_POWER = "samsungce.cooktopHeatingPower"
    SAMSUNG_CE_COOKTOP_PAN_DETECTION = "samsungce.cooktopPanDetection"
    SAMSUNG_CE_COUNT_DOWN_TIMER = "samsungce.countDownTimer"
    SAMSUNG_CE_CUSTOM_RECIPE = "samsungce.customRecipe"
    SAMSUNG_CE_DEFINED_RECIPE = "samsungce.definedRecipe"
    SAMSUNG_CE_DETERGENT_AUTO_REPLENISHMENT = "samsungce.detergentAutoReplenishment"
    SAMSUNG_CE_DETERGENT_ORDER = "samsungce.detergentOrder"
    SAMSUNG_CE_DETERGENT_STATE = "samsungce.detergentState"
    SAMSUNG_CE_DEVICE_IDENTIFICATION = "samsungce.deviceIdentification"
    SAMSUNG_CE_DISHWASHER_JOB_STATE = "samsungce.dishwasherJobState"
    SAMSUNG_CE_DISHWASHER_OPERATION = "samsungce.dishwasherOperation"
    SAMSUNG_CE_DISHWASHER_WASHING_COURSE = "samsungce.dishwasherWashingCourse"
    SAMSUNG_CE_DISHWASHER_WASHING_COURSE_DETAILS = (
        "samsungce.dishwasherWashingCourseDetails"
    )
    SAMSUNG_CE_DISHWASHER_WASHING_OPTIONS = "samsungce.dishwasherWashingOptions"
    SAMSUNG_CE_DO_NOT_DISTURB = "samsungce.doNotDisturb"
    SAMSUNG_CE_DONGLE_SOFTWARE_INSTALLATION = "samsungce.dongleSoftwareInstallation"
    SAMSUNG_CE_DOOR_STATE = "samsungce.doorState"
    SAMSUNG_CE_DRIVER_STATE = "samsungce.driverState"
    SAMSUNG_CE_DRIVER_VERSION = "samsungce.driverVersion"
    SAMSUNG_CE_DRUM_SELF_CLEANING = "samsungce.drumSelfCleaning"
    SAMSUNG_CE_DRYER_AUTO_CYCLE_LINK = "samsungce.dryerAutoCycleLink"
    SAMSUNG_CE_DRYER_CYCLE = "samsungce.dryerCycle"
    SAMSUNG_CE_DRYER_CYCLE_PRESET = "samsungce.dryerCyclePreset"
    SAMSUNG_CE_DRYER_DELAY_END = "samsungce.dryerDelayEnd"
    SAMSUNG_CE_DRYER_DRYING_TEMPERATURE = "samsungce.dryerDryingTemperature"
    SAMSUNG_CE_DRYER_DRYING_TIME = "samsungce.dryerDryingTime"
    SAMSUNG_CE_DRYER_FREEZE_PREVENT = "samsungce.dryerFreezePrevent"
    SAMSUNG_CE_DRYER_LABEL_SCAN_CYCLE_PRESET = "samsungce.dryerLabelScanCyclePreset"
    SAMSUNG_CE_DRYER_OPERATING_STATE = "samsungce.dryerOperatingState"
    SAMSUNG_CE_DUST_FILTER_ALARM = "samsungce.dustFilterAlarm"
    SAMSUNG_CE_EHS_CYCLE_DATA = "samsungce.ehsCycleData"
    SAMSUNG_CE_EHS_FSV_SETTINGS = "samsungce.ehsFsvSettings"
    SAMSUNG_CE_EHS_TEMPERATURE_REFERENCE = "samsungce.ehsTemperatureReference"
    SAMSUNG_CE_EHS_THERMOSTAT = "samsungce.ehsThermostat"
    SAMSUNG_CE_ENERGY_PLANNER = "samsungce.energyPlanner"
    SAMSUNG_CE_ERROR_AND_ALARM_STATE = "samsungce.errorAndAlarmState"
    SAMSUNG_CE_FLEXIBLE_AUTO_DISPENSE_DETERGENT = (
        "samsungce.flexibleAutoDispenseDetergent"
    )
    SAMSUNG_CE_FOOD_DEFROST = "samsungce.foodDefrost"
    SAMSUNG_CE_FREEZER_CONVERT_MODE = "samsungce.freezerConvertMode"
    SAMSUNG_CE_FRIDGE_FOOD_LIST = "samsungce.fridgeFoodList"
    SAMSUNG_CE_FRIDGE_PANTRY_INFO = "samsungce.fridgePantryInfo"
    SAMSUNG_CE_FRIDGE_PANTRY_MODE = "samsungce.fridgePantryMode"
    SAMSUNG_CE_FRIDGE_VACATION_MODE = "samsungce.fridgeVacationMode"
    SAMSUNG_CE_FRIDGE_WELCOME_LIGHTING = "samsungce.fridgeWelcomeLighting"
    SAMSUNG_CE_HOOD_FAN_SPEED = "samsungce.hoodFanSpeed"
    SAMSUNG_CE_HOOD_FILTER = "samsungce.hoodFilter"
    SAMSUNG_CE_HOOD_LAMP_AUTOMATION = "samsungce.hoodLampAutomation"
    SAMSUNG_CE_INDIVIDUAL_CONTROL_LOCK = "samsungce.individualControlLock"
    SAMSUNG_CE_KIDS_LOCK = "samsungce.kidsLock"
    SAMSUNG_CE_KIDS_LOCK_CONTROL = "samsungce.kidsLockControl"
    SAMSUNG_CE_KITCHEN_DEVICE_DEFAULTS = "samsungce.kitchenDeviceDefaults"
    SAMSUNG_CE_KITCHEN_DEVICE_IDENTIFICATION = "samsungce.kitchenDeviceIdentification"
    SAMSUNG_CE_KITCHEN_MODE_SPECIFICATION = "samsungce.kitchenModeSpecification"
    SAMSUNG_CE_LAMP = "samsungce.lamp"
    SAMSUNG_CE_MEAT_AGING = "samsungce.meatAging"
    SAMSUNG_CE_MEAT_PROBE = "samsungce.meatProbe"
    SAMSUNG_CE_MICROWAVE_POWER = "samsungce.microwavePower"
    SAMSUNG_CE_MUSIC_PLAYLIST = "samsungce.musicPlaylist"
    SAMSUNG_CE_NOTIFICATION = "samsungce.notification"
    SAMSUNG_CE_OPERATION_ORIGIN = "samsungce.operationOrigin"
    SAMSUNG_CE_OVEN_DRAINAGE_REQUIREMENT = "samsungce.ovenDrainageRequirement"
    SAMSUNG_CE_OVEN_MODE = "samsungce.ovenMode"
    SAMSUNG_CE_OVEN_OPERATING_STATE = "samsungce.ovenOperatingState"
    SAMSUNG_CE_POWER_CONSUMPTION_RECORD = "samsungce.powerConsumptionRecord"
    SAMSUNG_CE_POWER_COOL = "samsungce.powerCool"
    SAMSUNG_CE_POWER_FREEZE = "samsungce.powerFreeze"
    SAMSUNG_CE_QUICK_CONTROL = "samsungce.quickControl"
    SAMSUNG_CE_RECHARGEABLE_BATTERY = "samsungce.rechargeableBattery"
    SAMSUNG_CE_REMOTE_MANAGEMENT_DATA = "samsungce.remoteManagementData"
    SAMSUNG_CE_ROBOT_CLEANER_AUDIO_CLIP = "samsungce.robotCleanerAudioClip"
    SAMSUNG_CE_ROBOT_CLEANER_AVP_REGISTRATION = "samsungce.robotCleanerAvpRegistration"
    SAMSUNG_CE_ROBOT_CLEANER_CLEANING_MODE = "samsungce.robotCleanerCleaningMode"
    SAMSUNG_CE_ROBOT_CLEANER_DRIVING_MODE = "samsungce.robotCleanerDrivingMode"
    SAMSUNG_CE_ROBOT_CLEANER_DUST_BAG = "samsungce.robotCleanerDustBag"
    SAMSUNG_CE_ROBOT_CLEANER_FEATURE_VISIBILITY = (
        "samsungce.robotCleanerFeatureVisibility"
    )
    SAMSUNG_CE_ROBOT_CLEANER_MAP_AREA_INFO = "samsungce.robotCleanerMapAreaInfo"
    SAMSUNG_CE_ROBOT_CLEANER_MAP_CLEANING_INFO = "samsungce.robotCleanerMapCleaningInfo"
    SAMSUNG_CE_ROBOT_CLEANER_MAP_LIST = "samsungce.robotCleanerMapList"
    SAMSUNG_CE_ROBOT_CLEANER_MONITORING_AUTOMATION = (
        "samsungce.robotCleanerMonitoringAutomation"
    )
    SAMSUNG_CE_ROBOT_CLEANER_MOTOR_FILTER = "samsungce.robotCleanerMotorFilter"
    SAMSUNG_CE_ROBOT_CLEANER_OPERATING_STATE = "samsungce.robotCleanerOperatingState"
    SAMSUNG_CE_ROBOT_CLEANER_PATROL = "samsungce.robotCleanerPatrol"
    SAMSUNG_CE_ROBOT_CLEANER_PET_CLEANING_SCHEDULE = (
        "samsungce.robotCleanerPetCleaningSchedule"
    )
    SAMSUNG_CE_ROBOT_CLEANER_PET_MONITOR = "samsungce.robotCleanerPetMonitor"
    SAMSUNG_CE_ROBOT_CLEANER_PET_MONITOR_REPORT = (
        "samsungce.robotCleanerPetMonitorReport"
    )
    SAMSUNG_CE_ROBOT_CLEANER_RELAY_CLEANING = "samsungce.robotCleanerRelayCleaning"
    SAMSUNG_CE_ROBOT_CLEANER_RESERVATION = "samsungce.robotCleanerReservation"
    SAMSUNG_CE_ROBOT_CLEANER_WELCOME = "samsungce.robotCleanerWelcome"
    SAMSUNG_CE_RUNESTONE_HOME_CONTEXT = "samsungce.runestoneHomeContext"
    SAMSUNG_CE_SABBATH_MODE = "samsungce.sabbathMode"
    SAMSUNG_CE_SAC_DISPLAY_CONDITION = "samsungce.sacDisplayCondition"
    SAMSUNG_CE_SCALE_SETTINGS = "samsungce.scaleSettings"
    SAMSUNG_CE_SELF_CHECK = "samsungce.selfCheck"
    SAMSUNG_CE_SILENT_ACTION = "samsungce.silentAction"
    SAMSUNG_CE_SOFTENER_AUTO_REPLENISHMENT = "samsungce.softenerAutoReplenishment"
    SAMSUNG_CE_SOFTENER_ORDER = "samsungce.softenerOrder"
    SAMSUNG_CE_SOFTENER_STATE = "samsungce.softenerState"
    SAMSUNG_CE_SOFTWARE_UPDATE = "samsungce.softwareUpdate"
    SAMSUNG_CE_SOFTWARE_VERSION = "samsungce.softwareVersion"
    SAMSUNG_CE_SOUND_DETECTION_SENSITIVITY = "samsungce.soundDetectionSensitivity"
    SAMSUNG_CE_STEAM_CLOSET_AUTO_CYCLE_LINK = "samsungce.steamClosetAutoCycleLink"
    SAMSUNG_CE_STEAM_CLOSET_CYCLE = "samsungce.steamClosetCycle"
    SAMSUNG_CE_STEAM_CLOSET_CYCLE_PRESET = "samsungce.steamClosetCyclePreset"
    SAMSUNG_CE_STEAM_CLOSET_DELAY_END = "samsungce.steamClosetDelayEnd"
    SAMSUNG_CE_STEAM_CLOSET_KEEP_FRESH_MODE = "samsungce.steamClosetKeepFreshMode"
    SAMSUNG_CE_STEAM_CLOSET_SANITIZE_MODE = "samsungce.steamClosetSanitizeMode"
    SAMSUNG_CE_STICK_CLEANER_DUST_BAG = "samsungce.stickCleanerDustBag"
    SAMSUNG_CE_STICK_CLEANER_DUSTBIN_STATUS = "samsungce.stickCleanerDustbinStatus"
    SAMSUNG_CE_STICK_CLEANER_STATUS = "samsungce.stickCleanerStatus"
    SAMSUNG_CE_STICK_CLEANER_STICK_STATUS = "samsungce.stickCleanerStickStatus"
    SAMSUNG_CE_SURFACE_RESIDUAL_HEAT = "samsungce.surfaceResidualHeat"
    SAMSUNG_CE_TEMPERATURE_SETTING = "samsungce.temperatureSetting"
    SAMSUNG_CE_TOGGLE_SWITCH = "samsungce.toggleSwitch"
    SAMSUNG_CE_UNAVAILABLE_CAPABILITIES = "samsungce.unavailableCapabilities"
    SAMSUNG_CE_VIEW_INSIDE = "samsungce.viewInside"
    SAMSUNG_CE_WASHER_BUBBLE_SOAK = "samsungce.washerBubbleSoak"
    SAMSUNG_CE_WASHER_CYCLE = "samsungce.washerCycle"
    SAMSUNG_CE_WASHER_CYCLE_PRESET = "samsungce.washerCyclePreset"
    SAMSUNG_CE_WASHER_DELAY_END = "samsungce.washerDelayEnd"
    SAMSUNG_CE_WASHER_FREEZE_PREVENT = "samsungce.washerFreezePrevent"
    SAMSUNG_CE_WASHER_LABEL_SCAN_CYCLE_PRESET = "samsungce.washerLabelScanCyclePreset"
    SAMSUNG_CE_WASHER_OPERATING_STATE = "samsungce.washerOperatingState"
    SAMSUNG_CE_WASHER_WASHING_TIME = "samsungce.washerWashingTime"
    SAMSUNG_CE_WASHER_WATER_LEVEL = "samsungce.washerWaterLevel"
    SAMSUNG_CE_WASHER_WATER_VALVE = "samsungce.washerWaterValve"
    SAMSUNG_CE_WATER_CONSUMPTION_REPORT = "samsungce.waterConsumptionReport"
    SAMSUNG_CE_WATER_RESERVOIR = "samsungce.waterReservoir"
    SAMSUNG_CE_WEIGHT_MEASUREMENT = "samsungce.weightMeasurement"
    SAMSUNG_CE_WEIGHT_MEASUREMENT_CALIBRATION = "samsungce.weightMeasurementCalibration"
    SAMSUNG_CE_WELCOME_COOLING = "samsungce.welcomeCooling"
    SAMSUNG_CE_WELCOME_MESSAGE = "samsungce.welcomeMessage"
    SAMSUNG_CE_WIFI_KIT_SUB_DEVICES = "samsungce.wifiKitSubDevices"

    SAMSUNG_VD_AMBIENT = "samsungvd.ambient"
    SAMSUNG_VD_AMBIENT18 = "samsungvd.ambient18"
    SAMSUNG_VD_AMBIENT_CONTENT = "samsungvd.ambientContent"
    SAMSUNG_VD_AUDIO_GROUP_INFO = "samsungvd.audioGroupInfo"
    SAMSUNG_VD_AUDIO_INPUT_SOURCE = "samsungvd.audioInputSource"
    SAMSUNG_VD_DEVICE_CATEGORY = "samsungvd.deviceCategory"
    SAMSUNG_VD_FIRMWARE_VERSION = "samsungvd.firmwareVersion"
    SAMSUNG_VD_GROUP_INFO = "samsungvd.groupInfo"
    SAMSUNG_VD_LIGHT_CONTROL = "samsungvd.lightControl"
    SAMSUNG_VD_MEDIA_INPUT_SOURCE = "samsungvd.mediaInputSource"
    SAMSUNG_VD_PICTURE_MODE = "samsungvd.pictureMode"
    SAMSUNG_VD_REMOTE_CONTROL = "samsungvd.remoteControl"
    SAMSUNG_VD_SOUND_DETECTION = "samsungvd.soundDetection"
    SAMSUNG_VD_SOUND_FROM = "samsungvd.soundFrom"
    SAMSUNG_VD_SOUND_MODE = "samsungvd.soundMode"
    SAMSUNG_VD_SUPPORTS_FEATURES = "samsungvd.supportsFeatures"
    SAMSUNG_VD_SUPPORTS_POWER_ON_BY_OCF = "samsungvd.supportsPowerOnByOcf"
    SAMSUNG_VD_THING_STATUS = "samsungvd.thingStatus"

    SAMSUNG_IM_ANNOUNCEMENT = "samsungim.announcement"
    SAMSUNG_IM_BIXBY_CONTENT = "samsungim.bixbyContent"
    SAMSUNG_IM_CHARGER_FIRMWARE = "samsungim.chargerFirmware"
    SAMSUNG_IM_CHARGING_STATUS = "samsungim.chargingStatus"
    SAMSUNG_IM_DEVICESTATUS = "samsungim.devicestatus"
    SAMSUNG_IM_FIND_NODE = "samsungim.findNode"
    SAMSUNG_IM_FIND_NODE_GEOLOCATION = "samsungim.findNodeGeolocation"
    SAMSUNG_IM_FIRMWARE_AUTO_UPDATE = "samsungim.firmwareAutoUpdate"
    SAMSUNG_IM_FIRMWARE_SERVER = "samsungim.firmwareServer"
    SAMSUNG_IM_FIXED_FIND_NODE = "samsungim.fixedFindNode"
    SAMSUNG_IM_HUB_ONBOARDING = "samsungim.hubOnboarding"
    SAMSUNG_IM_HUE_SYNC_MODE = "samsungim.hueSyncMode"
    SAMSUNG_IM_LED_NOTIFICATION = "samsungim.ledNotification"
    SAMSUNG_IM_NEARBY_DETECTION = "samsungim.nearbyDetection"
    SAMSUNG_IM_NETWORK_AUDIO_GROUP_INFO = "samsungim.networkAudioGroupInfo"
    SAMSUNG_IM_NETWORK_AUDIO_MODE = "samsungim.networkAudioMode"
    SAMSUNG_IM_NETWORK_AUDIO_TRACK_DATA = "samsungim.networkAudioTrackData"
    SAMSUNG_IM_REQUEST_INVITATION = "samsungim.requestInvitation"
    SAMSUNG_IM_RING_MOBILE = "samsungim.ringMobile"
    SAMSUNG_IM_SAMSUNGACCOUNT = "samsungim.samsungaccount"
    SAMSUNG_IM_SELF_TEST = "samsungim.selfTest"
    SAMSUNG_IM_STHUBEUI = "samsungim.sthubeui"
    SAMSUNG_IM_WIFI = "samsungim.wifi"

    ABATEACHIEVE62503_STATELESS_AUDIO_MUTE = "abateachieve62503.statelessAudioMute"
    ABATEACHIEVE62503_STATELESS_AUDIO_VOLUME_DOWN = (
        "abateachieve62503.statelessAudioVolumeDown"
    )
    ABATEACHIEVE62503_STATELESS_AUDIO_VOLUME_UP = (
        "abateachieve62503.statelessAudioVolumeUp"
    )
    ABATEACHIEVE62503_STATELESS_CHANNEL_DOWN = "abateachieve62503.statelessChannelDown"
    ABATEACHIEVE62503_STATELESS_CHANNEL_UP = "abateachieve62503.statelessChannelUp"

    ABSOLUTEWEATHER46907_LANGUAGE_SUPPORT = "absoluteweather46907.languageSupport"
    ABSOLUTEWEATHER46907_LOCK = "absoluteweather46907.lock"
    ABSOLUTEWEATHER46907_LOCKSTATERELEASE = "absoluteweather46907.lockstaterelease"

    AMBERPIANO10217_BINDING_INFO = "amberpiano10217.bindingInfo"
    AMBERPIANO10217_CLUSTER = "amberpiano10217.cluster"
    AMBERPIANO10217_CONTROLLER_STATUS = "amberpiano10217.controllerStatus"
    AMBERPIANO10217_DETECTION_INTERVAL = "amberpiano10217.detectionInterval"
    AMBERPIANO10217_DEVICE_EUI = "amberpiano10217.deviceEui"
    AMBERPIANO10217_DEVICEINFO = "amberpiano10217.deviceinfo"
    AMBERPIANO10217_GROUP_ADD = "amberpiano10217.groupAdd"
    AMBERPIANO10217_GROUP_INFO = "amberpiano10217.groupInfo"
    AMBERPIANO10217_GROUP_REMOVE = "amberpiano10217.groupRemove"
    AMBERPIANO10217_GROUP_REMOVE_ALL = "amberpiano10217.groupRemoveAll"
    AMBERPIANO10217_OBJECT = "amberpiano10217.object"
    AMBERPIANO10217_SENSOR_DETECTION_SENSITIVITY = (
        "amberpiano10217.sensorDetectionSensitivity"
    )
    AMBERPIANO10217_VIRTUAL_THING_TYPE = "amberpiano10217.virtualThingType"

    EVENTFLUTE36860_DEFAULT_LEVEL_LOCAL = "eventflute36860.defaultLevelLocal"
    EVENTFLUTE36860_LED_BAR_SWITCH_OFF = "eventflute36860.ledBarSwitchOff"
    EVENTFLUTE36860_LED_BAR_SWITCH_ON = "eventflute36860.ledBarSwitchOn"
    EVENTFLUTE36860_LOCAL_CONTROL = "eventflute36860.localControl"
    EVENTFLUTE36860_LOG = "eventflute36860.log"
    EVENTFLUTE36860_NOTIFICATION_ALL = "eventflute36860.notificationAll"
    EVENTFLUTE36860_NOTIFICATION_SINGLE = "eventflute36860.notificationSingle"
    EVENTFLUTE36860_REMOTE_CONTROL = "eventflute36860.remoteControl"

    HCA_DRYER_MODE = "hca.dryerMode"
    HCA_WASHER_MODE = "hca.washerMode"

    LEGENDABSOLUTE60149_ATMOS_PRESSURE = "legendabsolute60149.atmosPressure"
    LEGENDABSOLUTE60149_CIRCADIAN = "legendabsolute60149.circadian"
    LEGENDABSOLUTE60149_COLOR_CHANGE_MODE1 = "legendabsolute60149.colorChangeMode1"
    LEGENDABSOLUTE60149_COLOR_CHANGE_TIMER = "legendabsolute60149.colorChangeTimer"
    LEGENDABSOLUTE60149_COLOR_CHANGING = "legendabsolute60149.colorChanging"
    LEGENDABSOLUTE60149_COLOR_TEMPERATURE_STEPS = (
        "legendabsolute60149.colorTemperatureSteps"
    )
    LEGENDABSOLUTE60149_CREATE_DEVICE2 = "legendabsolute60149.createDevice2"
    LEGENDABSOLUTE60149_CURRENT_LOOP = "legendabsolute60149.currentLoop"
    LEGENDABSOLUTE60149_CURRENT_TIME_PERIOD = "legendabsolute60149.currentTimePeriod"
    LEGENDABSOLUTE60149_CURRENT_TWILIGHT = "legendabsolute60149.currentTwilight"
    LEGENDABSOLUTE60149_DAY_LENGTH = "legendabsolute60149.dayLength"
    LEGENDABSOLUTE60149_DRIVER_VERSION1 = "legendabsolute60149.driverVersion1"
    LEGENDABSOLUTE60149_EFFECTS_SET_COMMAND = "legendabsolute60149.effectsSetCommand"
    LEGENDABSOLUTE60149_ENERGY_RESET1 = "legendabsolute60149.energyReset1"
    LEGENDABSOLUTE60149_EVEN_ODD_DAY = "legendabsolute60149.evenOddDay"
    LEGENDABSOLUTE60149_FORCED_ON_LEVEL = "legendabsolute60149.forcedOnLevel"
    LEGENDABSOLUTE60149_GET_GROUPS = "legendabsolute60149.getGroups"
    LEGENDABSOLUTE60149_HUE_STEPS = "legendabsolute60149.hueSteps"
    LEGENDABSOLUTE60149_HUMIDITY_CONDITION = "legendabsolute60149.humidityCondition"
    LEGENDABSOLUTE60149_HUMIDITY_TARGET = "legendabsolute60149.humidityTarget"
    LEGENDABSOLUTE60149_LEVEL_STEPS = "legendabsolute60149.levelSteps"
    LEGENDABSOLUTE60149_LOCAL_DATE = "legendabsolute60149.localDate"
    LEGENDABSOLUTE60149_LOCAL_DATE_ONE = "legendabsolute60149.localDateOne"
    LEGENDABSOLUTE60149_LOCAL_DATE_TWO1 = "legendabsolute60149.localDateTwo1"
    LEGENDABSOLUTE60149_LOCAL_DAY = "legendabsolute60149.localDay"
    LEGENDABSOLUTE60149_LOCAL_DAY_TWO = "legendabsolute60149.localDayTwo"
    LEGENDABSOLUTE60149_LOCAL_HOUR = "legendabsolute60149.localHour"
    LEGENDABSOLUTE60149_LOCAL_HOUR_OFFSET = "legendabsolute60149.localHourOffset"
    LEGENDABSOLUTE60149_LOCAL_HOUR_TWO = "legendabsolute60149.localHourTwo"
    LEGENDABSOLUTE60149_LOCAL_MONTH = "legendabsolute60149.localMonth"
    LEGENDABSOLUTE60149_LOCAL_MONTH_DAY_ONE = "legendabsolute60149.localMonthDayOne"
    LEGENDABSOLUTE60149_LOCAL_MONTH_DAY_TWO = "legendabsolute60149.localMonthDayTwo"
    LEGENDABSOLUTE60149_LOCAL_MONTH_TWO = "legendabsolute60149.localMonthTwo"
    LEGENDABSOLUTE60149_LOCAL_WEEK_DAY = "legendabsolute60149.localWeekDay"
    LEGENDABSOLUTE60149_LOCAL_YEAR = "legendabsolute60149.localYear"
    LEGENDABSOLUTE60149_LOOPS_NUMBER = "legendabsolute60149.loopsNumber"
    LEGENDABSOLUTE60149_MIRROR_GROUP_FUNCTION = (
        "legendabsolute60149.mirrorGroupFunction"
    )
    LEGENDABSOLUTE60149_MIRROR_IN = "legendabsolute60149.mirrorIn"
    LEGENDABSOLUTE60149_MIRROR_OUT = "legendabsolute60149.mirrorOut"
    LEGENDABSOLUTE60149_PROGRESSIVE_OFF1 = "legendabsolute60149.progressiveOff1"
    LEGENDABSOLUTE60149_PROGRESSIVE_ON1 = "legendabsolute60149.progressiveOn1"
    LEGENDABSOLUTE60149_RANDOM_MAXIMUM_TIMER = "legendabsolute60149.randomMaximumTimer"
    LEGENDABSOLUTE60149_RANDOM_MINIMUM_TIMER = "legendabsolute60149.randomMinimumTimer"
    LEGENDABSOLUTE60149_RANDOM_NEXT_STEP = "legendabsolute60149.randomNextStep"
    LEGENDABSOLUTE60149_RANDOM_NEXT_STEP2 = "legendabsolute60149.randomNextStep2"
    LEGENDABSOLUTE60149_RANDOM_ON_OFF1 = "legendabsolute60149.randomOnOff1"
    LEGENDABSOLUTE60149_RANDOM_ON_OFF2 = "legendabsolute60149.randomOnOff2"
    LEGENDABSOLUTE60149_RESETBUTTON = "legendabsolute60149.resetbutton"
    LEGENDABSOLUTE60149_SIGNAL_METRICS = "legendabsolute60149.signalMetrics"
    LEGENDABSOLUTE60149_SUN_AZIMUTH_ANGLE = "legendabsolute60149.sunAzimuthAngle"
    LEGENDABSOLUTE60149_SUN_ELEVATION_ANGLE = "legendabsolute60149.sunElevationAngle"
    LEGENDABSOLUTE60149_SUN_RISE = "legendabsolute60149.sunRise"
    LEGENDABSOLUTE60149_SUN_RISE_OFFSET1 = "legendabsolute60149.sunRiseOffset1"
    LEGENDABSOLUTE60149_SUN_SET = "legendabsolute60149.sunSet"
    LEGENDABSOLUTE60149_SUN_SET_OFFSET1 = "legendabsolute60149.sunSetOffset1"
    LEGENDABSOLUTE60149_SWITCH_ALL_ON_OFF1 = "legendabsolute60149.switchAllOnOff1"
    LEGENDABSOLUTE60149_TEMP_CONDITION2 = "legendabsolute60149.tempCondition2"
    LEGENDABSOLUTE60149_TEMP_TARGET = "legendabsolute60149.tempTarget"
    LEGENDABSOLUTE60149_TIMER_NEXT_CHANGE = "legendabsolute60149.timerNextChange"
    LEGENDABSOLUTE60149_TIMER_SECONDS = "legendabsolute60149.timerSeconds"
    LEGENDABSOLUTE60149_TIMER_TYPE = "legendabsolute60149.timerType"

    MUSICAHEAD43206_POWERMODE = "musicahead43206.powermode"
    MUSICAHEAD43206_SNOOZE = "musicahead43206.snooze"
    MUSICAHEAD43206_STAGE = "musicahead43206.stage"

    PARTYVOICE23922_ADD2 = "partyvoice23922.add2"
    PARTYVOICE23922_AMPERAGE = "partyvoice23922.amperage"
    PARTYVOICE23922_APIWEBREQUEST = "partyvoice23922.apiwebrequest"
    PARTYVOICE23922_BAROMETER2 = "partyvoice23922.barometer2"
    PARTYVOICE23922_CASTMEDIACONTROL = "partyvoice23922.castmediacontrol"
    PARTYVOICE23922_CLOSEDURATION = "partyvoice23922.closeduration"
    PARTYVOICE23922_CLOUDCOVER = "partyvoice23922.cloudcover"
    PARTYVOICE23922_COUNT = "partyvoice23922.count"
    PARTYVOICE23922_CREATEANOTHER = "partyvoice23922.createanother"
    PARTYVOICE23922_CREATEDEV8 = "partyvoice23922.createdev8"
    PARTYVOICE23922_CREATEHTTPDEV2B = "partyvoice23922.createhttpdev2b"
    PARTYVOICE23922_CREATEMQTTDEV9 = "partyvoice23922.createmqttdev9"
    PARTYVOICE23922_CREATEQTY = "partyvoice23922.createqty"
    PARTYVOICE23922_DURATION2 = "partyvoice23922.duration2"
    PARTYVOICE23922_ERRORSENSOR = "partyvoice23922.errorsensor"
    PARTYVOICE23922_ERRORSTATUS = "partyvoice23922.errorstatus"
    PARTYVOICE23922_ERRORSTATUSCV = "partyvoice23922.errorstatuscv"
    PARTYVOICE23922_HTTPCODE = "partyvoice23922.httpcode"
    PARTYVOICE23922_HTTPRESPONSE = "partyvoice23922.httpresponse"
    PARTYVOICE23922_INFOTABLE = "partyvoice23922.infotable"
    PARTYVOICE23922_INPUTPERCENT = "partyvoice23922.inputpercent"
    PARTYVOICE23922_INPUTSTATE = "partyvoice23922.inputstate"
    PARTYVOICE23922_INVENTORY8 = "partyvoice23922.inventory8"
    PARTYVOICE23922_KEYNUMVALUE = "partyvoice23922.keynumvalue"
    PARTYVOICE23922_KEYVALUE2 = "partyvoice23922.keyvalue2"
    PARTYVOICE23922_LOCATION = "partyvoice23922.location"
    PARTYVOICE23922_MEDIASUBTITLE = "partyvoice23922.mediasubtitle"
    PARTYVOICE23922_MEDIATITLE = "partyvoice23922.mediatitle"
    PARTYVOICE23922_MQTTPUBLISH = "partyvoice23922.mqttpublish"
    PARTYVOICE23922_NAMEINPUT = "partyvoice23922.nameinput"
    PARTYVOICE23922_ONVIFINFO = "partyvoice23922.onvifinfo"
    PARTYVOICE23922_ONVIFSTATUS = "partyvoice23922.onvifstatus"
    PARTYVOICE23922_OPENDURATION = "partyvoice23922.openduration"
    PARTYVOICE23922_POWERFACTOR2 = "partyvoice23922.powerfactor2"
    PARTYVOICE23922_PRECIPPROB = "partyvoice23922.precipprob"
    PARTYVOICE23922_PRECIPRATE = "partyvoice23922.preciprate"
    PARTYVOICE23922_REACTIVEPOWER = "partyvoice23922.reactivepower"
    PARTYVOICE23922_REFRESH = "partyvoice23922.refresh"
    PARTYVOICE23922_RESETALT = "partyvoice23922.resetalt"
    PARTYVOICE23922_RESETSELECT = "partyvoice23922.resetselect"
    PARTYVOICE23922_ROKUCURRENTAPP = "partyvoice23922.rokucurrentapp"
    PARTYVOICE23922_ROKUMEDIASTATUS = "partyvoice23922.rokumediastatus"
    PARTYVOICE23922_SETILLUMINANCE = "partyvoice23922.setilluminance"
    PARTYVOICE23922_SHADEPAUSE = "partyvoice23922.shadepause"
    PARTYVOICE23922_SHELLYDEVS4 = "partyvoice23922.shellydevs4"
    PARTYVOICE23922_STATEFIELD2 = "partyvoice23922.statefield2"
    PARTYVOICE23922_STATUS = "partyvoice23922.status"
    PARTYVOICE23922_SUBTRACT2 = "partyvoice23922.subtract2"
    PARTYVOICE23922_SUMMARY = "partyvoice23922.summary"
    PARTYVOICE23922_TEMPMAX = "partyvoice23922.tempmax"
    PARTYVOICE23922_TEMPMIN = "partyvoice23922.tempmin"
    PARTYVOICE23922_TOPICLIST = "partyvoice23922.topiclist"
    PARTYVOICE23922_TVCHANNEL = "partyvoice23922.tvchannel"
    PARTYVOICE23922_VHUMIDITYSET = "partyvoice23922.vhumidityset"
    PARTYVOICE23922_VOLUMEDOWN = "partyvoice23922.volumedown"
    PARTYVOICE23922_VOLUMEUP = "partyvoice23922.volumeup"
    PARTYVOICE23922_VTEMPSET = "partyvoice23922.vtempset"
    PARTYVOICE23922_WEBREQUEST = "partyvoice23922.webrequest"
    PARTYVOICE23922_WEBREQUESTSELECT = "partyvoice23922.webrequestselect"
    PARTYVOICE23922_WINDDIRDEG = "partyvoice23922.winddirdeg"
    PARTYVOICE23922_WINDDIRECTION2 = "partyvoice23922.winddirection2"
    PARTYVOICE23922_WINDGUST = "partyvoice23922.windgust"
    PARTYVOICE23922_WINDSPEED5 = "partyvoice23922.windspeed5"

    PLATEMUSIC11009_ASSOCIATION_GROUP_FOUR = "platemusic11009.associationGroupFour"
    PLATEMUSIC11009_ASSOCIATION_GROUP_THREE = "platemusic11009.associationGroupThree"
    PLATEMUSIC11009_ASSOCIATION_GROUP_TWO = "platemusic11009.associationGroupTwo"
    PLATEMUSIC11009_DEVICE_NETWORK_ID = "platemusic11009.deviceNetworkId"
    PLATEMUSIC11009_FIRMWARE = "platemusic11009.firmware"

    RBOYAPPS_LOCK_AUDIO = "rboyapps.lockAudio"
    RBOYAPPS_LOCK_AUTOLOCK = "rboyapps.lockAutolock"
    RBOYAPPS_LOCK_EXTENDED = "rboyapps.lockExtended"
    RBOYAPPS_LOCK_KEYPAD = "rboyapps.lockKeypad"
    RBOYAPPS_LOCK_ONE_TOUCH_LOCK = "rboyapps.lockOneTouchLock"
    RBOYAPPS_LOCK_TAMPER = "rboyapps.lockTamper"
    RBOYAPPS_LOCK_TAMPER_SENSITIVITY = "rboyapps.lockTamperSensitivity"

    RIVERTALENT14263_ADAPTIVE_ENERGY_USAGE_STATE = (
        "rivertalent14263.adaptiveEnergyUsageState"
    )
    RIVERTALENT14263_BATCH_POWER_CONSUMPTION_REPORT = (
        "rivertalent14263.batchPowerConsumptionReport"
    )
    RIVERTALENT14263_ENERGY_METER_PROPERTIES = "rivertalent14263.energyMeterProperties"

    SEC_CALM_CONNECTION_CARE = "sec.calmConnectionCare"
    SEC_DEVICE_CONNECTION_STATE = "sec.deviceConnectionState"
    SEC_DIAGNOSTICS_INFORMATION = "sec.diagnosticsInformation"
    SEC_WIFI_CONFIGURATION = "sec.wifiConfiguration"

    STSOLUTIONS_DEMAND_RESPONSE_STATUS = "stsolutions.demandResponseStatus"

    SYNTHETIC_CIRCADIAN_LIGHTING_EFFECT = "synthetic.lightingEffectCircadian"
    SYNTHETIC_FADE_LIGHTNING_EFFECT = "synthetic.lightingEffectFade"

    TAG_E2E_ENCRYPTION = "tag.e2eEncryption"
    TAG_FACTORY_RESET = "tag.factoryReset"
    TAG_SEARCHING_STATUS = "tag.searchingStatus"
    TAG_TAG_BUTTON = "tag.tagButton"
    TAG_TAG_STATUS = "tag.tagStatus"
    TAG_UPDATED_INFO = "tag.updatedInfo"
    TAG_UWB_ACTIVATION = "tag.uwbActivation"

    VALLEYBOARD16460_DEBUG = "valleyboard16460.debug"
    VALLEYBOARD16460_INFO = "valleyboard16460.info"

    WATCHPANEL55613_LCCTHERMOSTAT = "watchpanel55613.lccthermostat"
