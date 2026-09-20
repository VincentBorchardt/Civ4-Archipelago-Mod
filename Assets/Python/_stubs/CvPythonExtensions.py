"""
CvPythonExtensions

Civilization IV Player Class
"""

class ActionSubTypes :
	ACTIONSUBTYPE_AUTOMATE = 10 # type: ActionSubTypes
	ACTIONSUBTYPE_BUILD = 2 # type: ActionSubTypes
	ACTIONSUBTYPE_BUILDING = 8 # type: ActionSubTypes
	ACTIONSUBTYPE_COMMAND = 1 # type: ActionSubTypes
	ACTIONSUBTYPE_CONTROL = 9 # type: ActionSubTypes
	ACTIONSUBTYPE_INTERFACEMODE = 0 # type: ActionSubTypes
	ACTIONSUBTYPE_MISSION = 11 # type: ActionSubTypes
	ACTIONSUBTYPE_PROMOTION = 3 # type: ActionSubTypes
	ACTIONSUBTYPE_RELIGION = 5 # type: ActionSubTypes
	ACTIONSUBTYPE_SPECIALIST = 7 # type: ActionSubTypes
	ACTIONSUBTYPE_UNIT = 4 # type: ActionSubTypes
	NO_ACTIONSUBTYPE = -1 # type: ActionSubTypes
	NUM_ACTIONSUBTYPES = 12 # type: ActionSubTypes

class ActivationTypes :
	ACTIVATE_CHILDFOCUS = 1 # type: ActivationTypes
	ACTIVATE_MIMICPARENT = 2 # type: ActivationTypes
	ACTIVATE_MIMICPARENTFOCUS = 3 # type: ActivationTypes
	ACTIVATE_NORMAL = 0 # type: ActivationTypes

class ActivityTypes :
	ACTIVITY_AWAKE = 0 # type: ActivityTypes
	ACTIVITY_HEAL = 3 # type: ActivityTypes
	ACTIVITY_HOLD = 1 # type: ActivityTypes
	ACTIVITY_INTERCEPT = 5 # type: ActivityTypes
	ACTIVITY_MISSION = 6 # type: ActivityTypes
	ACTIVITY_PATROL = 7 # type: ActivityTypes
	ACTIVITY_PLUNDER = 8 # type: ActivityTypes
	ACTIVITY_SENTRY = 4 # type: ActivityTypes
	ACTIVITY_SLEEP = 2 # type: ActivityTypes
	NO_ACTIVITY = -1 # type: ActivityTypes
	NUM_ACTIVITY_TYPES = 9 # type: ActivityTypes

class AdvancedStartActionTypes :
	ADVANCEDSTARTACTION_AUTOMATE = 10 # type: AdvancedStartActionTypes
	ADVANCEDSTARTACTION_BUILDING = 5 # type: AdvancedStartActionTypes
	ADVANCEDSTARTACTION_CITY = 2 # type: AdvancedStartActionTypes
	ADVANCEDSTARTACTION_CULTURE = 4 # type: AdvancedStartActionTypes
	ADVANCEDSTARTACTION_EXIT = 0 # type: AdvancedStartActionTypes
	ADVANCEDSTARTACTION_IMPROVEMENT = 6 # type: AdvancedStartActionTypes
	ADVANCEDSTARTACTION_POP = 3 # type: AdvancedStartActionTypes
	ADVANCEDSTARTACTION_ROUTE = 7 # type: AdvancedStartActionTypes
	ADVANCEDSTARTACTION_TECH = 8 # type: AdvancedStartActionTypes
	ADVANCEDSTARTACTION_UNIT = 1 # type: AdvancedStartActionTypes
	ADVANCEDSTARTACTION_VISIBILITY = 9 # type: AdvancedStartActionTypes
	NO_ADVANCEDSTARTACTION = -1 # type: AdvancedStartActionTypes

class AdvisorTypes :
	NO_ADVISOR = -1 # type: AdvisorTypes

class AnimationCategoryTypes :
	ANIMCAT_NONE = -1 # type: AnimationCategoryTypes

class AnimationPathTypes :
	ANIMATIONPATH_AIRBOMB = 21 # type: AnimationPathTypes
	ANIMATIONPATH_AIRFADEIN = 18 # type: AnimationPathTypes
	ANIMATIONPATH_AIRFADEOUT = 19 # type: AnimationPathTypes
	ANIMATIONPATH_AIRSTRIKE = 20 # type: AnimationPathTypes
	ANIMATIONPATH_IDLE = 0 # type: AnimationPathTypes
	ANIMATIONPATH_LEADER_COMMAND = 17 # type: AnimationPathTypes
	ANIMATIONPATH_MELEE_DIE = 7 # type: AnimationPathTypes
	ANIMATIONPATH_MELEE_DIE_FADE = 9 # type: AnimationPathTypes
	ANIMATIONPATH_MELEE_FORTIFIED = 8 # type: AnimationPathTypes
	ANIMATIONPATH_MELEE_HURT = 6 # type: AnimationPathTypes
	ANIMATIONPATH_MELEE_STRIKE = 5 # type: AnimationPathTypes
	ANIMATIONPATH_MOVE = 1 # type: AnimationPathTypes
	ANIMATIONPATH_NONE = -1 # type: AnimationPathTypes
	ANIMATIONPATH_NUKE_STRIKE = 4 # type: AnimationPathTypes
	ANIMATIONPATH_RANDOMIZE_ANIMATION_SET = 3 # type: AnimationPathTypes
	ANIMATIONPATH_RANGED_DIE = 12 # type: AnimationPathTypes
	ANIMATIONPATH_RANGED_DIE_FADE = 16 # type: AnimationPathTypes
	ANIMATIONPATH_RANGED_FORTIFIED = 13 # type: AnimationPathTypes
	ANIMATIONPATH_RANGED_RUNDIE = 15 # type: AnimationPathTypes
	ANIMATIONPATH_RANGED_RUNHIT = 14 # type: AnimationPathTypes
	ANIMATIONPATH_RANGED_STRIKE = 11 # type: AnimationPathTypes

class AnimationTypes :
	BONUSANIMATION_NOT_WORKED = 2 # type: AnimationTypes
	BONUSANIMATION_UNIMPROVED = 1 # type: AnimationTypes
	BONUSANIMATION_WORKED = 3 # type: AnimationTypes
	IMPROVEMENTANIMATION_OFF = 2 # type: AnimationTypes
	IMPROVEMENTANIMATION_OFF_EXTRA = 4 # type: AnimationTypes
	IMPROVEMENTANIMATION_ON = 3 # type: AnimationTypes
	IMPROVEMENTANIMATION_ON_EXTRA_1 = 5 # type: AnimationTypes
	IMPROVEMENTANIMATION_ON_EXTRA_2 = 6 # type: AnimationTypes
	IMPROVEMENTANIMATION_ON_EXTRA_3 = 7 # type: AnimationTypes
	IMPROVEMENTANIMATION_ON_EXTRA_4 = 8 # type: AnimationTypes
	NONE_ANIMATION = -1 # type: AnimationTypes

class AreaAITypes :
	AREAAI_ASSAULT = 3 # type: AreaAITypes
	AREAAI_DEFENSIVE = 1 # type: AreaAITypes
	AREAAI_MASSING = 2 # type: AreaAITypes
	AREAAI_NEUTRAL = 6 # type: AreaAITypes
	AREAAI_OFFENSIVE = 0 # type: AreaAITypes
	NO_AREAAI = -1 # type: AreaAITypes

class AreaBorderLayers :
	AREA_BORDER_LAYER_BLOCKADED = 7 # type: AreaBorderLayers
	AREA_BORDER_LAYER_BLOCKADING = 6 # type: AreaBorderLayers
	AREA_BORDER_LAYER_CITY_RADIUS = 3 # type: AreaBorderLayers
	AREA_BORDER_LAYER_FOUNDING_BORDER = 2 # type: AreaBorderLayers
	AREA_BORDER_LAYER_HIGHLIGHT_PLOT = 5 # type: AreaBorderLayers
	AREA_BORDER_LAYER_RANGED = 4 # type: AreaBorderLayers
	AREA_BORDER_LAYER_REVEALED_PLOTS = 0 # type: AreaBorderLayers
	AREA_BORDER_LAYER_WORLD_BUILDER = 1 # type: AreaBorderLayers
	NUM_AREA_BORDER_LAYERS = 8 # type: AreaBorderLayers

class ArtStyleTypes :
	NO_ARTSTYLE = -1 # type: ArtStyleTypes

class AttitudeTypes :
	ATTITUDE_ANNOYED = 1 # type: AttitudeTypes
	ATTITUDE_CAUTIOUS = 2 # type: AttitudeTypes
	ATTITUDE_FRIENDLY = 4 # type: AttitudeTypes
	ATTITUDE_FURIOUS = 0 # type: AttitudeTypes
	ATTITUDE_PLEASED = 3 # type: AttitudeTypes
	NO_ATTITUDE = -1 # type: AttitudeTypes
	NUM_ATTITUDE_TYPES = 5 # type: AttitudeTypes

class AudioTag :
	AUDIOTAG_2DSCRIPT = 3 # type: AudioTag
	AUDIOTAG_3DSCRIPT = 4 # type: AudioTag
	AUDIOTAG_CONTEXTID = 1 # type: AudioTag
	AUDIOTAG_COUNT = 9 # type: AudioTag
	AUDIOTAG_LOADTYPE = 8 # type: AudioTag
	AUDIOTAG_NONE = -1 # type: AudioTag
	AUDIOTAG_POSITION = 6 # type: AudioTag
	AUDIOTAG_SCRIPTTYPE = 7 # type: AudioTag
	AUDIOTAG_SOUNDID = 0 # type: AudioTag
	AUDIOTAG_SOUNDSCAPE = 5 # type: AudioTag
	AUDIOTAG_SOUNDTYPE = 2 # type: AudioTag

class AutomateTypes :
	AUTOMATE_BUILD = 0 # type: AutomateTypes
	AUTOMATE_CITY = 2 # type: AutomateTypes
	AUTOMATE_EXPLORE = 3 # type: AutomateTypes
	AUTOMATE_NETWORK = 1 # type: AutomateTypes
	AUTOMATE_RELIGION = 4 # type: AutomateTypes
	NO_AUTOMATE = -1 # type: AutomateTypes
	NUM_AUTOMATE_TYPES = 5 # type: AutomateTypes

class BonusClassTypes :
	NO_BONUSCLASS = -1 # type: BonusClassTypes

class BonusTypes :
	NO_BONUS = -1 # type: BonusTypes

class BuildTypes :
	NO_BUILD = -1 # type: BuildTypes

class BuildingClassTypes :
	NO_BUILDINGCLASS = -1 # type: BuildingClassTypes

class BuildingTypes :
	NO_BUILDING = -1 # type: BuildingTypes

class ButtonPopupTypes :
	BUTTONPOPUP_ADDBUDDY = 26 # type: ButtonPopupTypes
	BUTTONPOPUP_ADMIN = 22 # type: ButtonPopupTypes
	BUTTONPOPUP_ADMIN_PASSWORD = 23 # type: ButtonPopupTypes
	BUTTONPOPUP_ALARM = 17 # type: ButtonPopupTypes
	BUTTONPOPUP_CHANGECIVIC = 13 # type: ButtonPopupTypes
	BUTTONPOPUP_CHANGERELIGION = 14 # type: ButtonPopupTypes
	BUTTONPOPUP_CHOOSEELECTION = 15 # type: ButtonPopupTypes
	BUTTONPOPUP_CHOOSEPRODUCTION = 12 # type: ButtonPopupTypes
	BUTTONPOPUP_CHOOSETECH = 9 # type: ButtonPopupTypes
	BUTTONPOPUP_CONFIRMCOMMAND = 4 # type: ButtonPopupTypes
	BUTTONPOPUP_CONFIRM_MENU = 2 # type: ButtonPopupTypes
	BUTTONPOPUP_DEAL_CANCELED = 18 # type: ButtonPopupTypes
	BUTTONPOPUP_DECLAREWARMOVE = 3 # type: ButtonPopupTypes
	BUTTONPOPUP_DETAILS = 21 # type: ButtonPopupTypes
	BUTTONPOPUP_DIPLOMACY = 25 # type: ButtonPopupTypes
	BUTTONPOPUP_DIPLOVOTE = 16 # type: ButtonPopupTypes
	BUTTONPOPUP_DISBANDCITY = 11 # type: ButtonPopupTypes
	BUTTONPOPUP_DOESPIONAGE = 7 # type: ButtonPopupTypes
	BUTTONPOPUP_DOESPIONAGE_TARGET = 8 # type: ButtonPopupTypes
	BUTTONPOPUP_EVENT = 32 # type: ButtonPopupTypes
	BUTTONPOPUP_EXTENDED_GAME = 24 # type: ButtonPopupTypes
	BUTTONPOPUP_FORCED_DISCONNECT = 27 # type: ButtonPopupTypes
	BUTTONPOPUP_FOUND_RELIGION = 35 # type: ButtonPopupTypes
	BUTTONPOPUP_FREE_COLONY = 33 # type: ButtonPopupTypes
	BUTTONPOPUP_KICKED = 28 # type: ButtonPopupTypes
	BUTTONPOPUP_LAUNCH = 34 # type: ButtonPopupTypes
	BUTTONPOPUP_LEADUNIT = 6 # type: ButtonPopupTypes
	BUTTONPOPUP_LOADUNIT = 5 # type: ButtonPopupTypes
	BUTTONPOPUP_MAIN_MENU = 1 # type: ButtonPopupTypes
	BUTTONPOPUP_PITBOSS_DISCONNECT = 28 # type: ButtonPopupTypes
	BUTTONPOPUP_PYTHON = 19 # type: ButtonPopupTypes
	BUTTONPOPUP_PYTHON_SCREEN = 20 # type: ButtonPopupTypes
	BUTTONPOPUP_RAZECITY = 10 # type: ButtonPopupTypes
	BUTTONPOPUP_TEXT = 0 # type: ButtonPopupTypes
	BUTTONPOPUP_VASSAL_DEMAND_TRIBUTE = 30 # type: ButtonPopupTypes
	BUTTONPOPUP_VASSAL_GRANT_TRIBUTE = 31 # type: ButtonPopupTypes
	NUM_BUTTONPOPUP_TYPES = 36 # type: ButtonPopupTypes

class ButtonStyles :
	BUTTON_STYLE_ARROW_LEFT = 24 # type: ButtonStyles
	BUTTON_STYLE_ARROW_RIGHT = 25 # type: ButtonStyles
	BUTTON_STYLE_CIRCLE = 9 # type: ButtonStyles
	BUTTON_STYLE_CITY_B01 = 10 # type: ButtonStyles
	BUTTON_STYLE_CITY_B02BL = 13 # type: ButtonStyles
	BUTTON_STYLE_CITY_B02BR = 14 # type: ButtonStyles
	BUTTON_STYLE_CITY_B02TL = 11 # type: ButtonStyles
	BUTTON_STYLE_CITY_B02TR = 12 # type: ButtonStyles
	BUTTON_STYLE_CITY_B03BC = 19 # type: ButtonStyles
	BUTTON_STYLE_CITY_B03BL = 18 # type: ButtonStyles
	BUTTON_STYLE_CITY_B03BR = 20 # type: ButtonStyles
	BUTTON_STYLE_CITY_B03TC = 16 # type: ButtonStyles
	BUTTON_STYLE_CITY_B03TL = 15 # type: ButtonStyles
	BUTTON_STYLE_CITY_B03TR = 17 # type: ButtonStyles
	BUTTON_STYLE_CITY_FLAT = 21 # type: ButtonStyles
	BUTTON_STYLE_CITY_MINUS = 23 # type: ButtonStyles
	BUTTON_STYLE_CITY_PLUS = 22 # type: ButtonStyles
	BUTTON_STYLE_DEFAULT = 8 # type: ButtonStyles
	BUTTON_STYLE_ETCHED = 1 # type: ButtonStyles
	BUTTON_STYLE_FLAT = 2 # type: ButtonStyles
	BUTTON_STYLE_IMAGE = 3 # type: ButtonStyles
	BUTTON_STYLE_LABEL = 4 # type: ButtonStyles
	BUTTON_STYLE_LINK = 5 # type: ButtonStyles
	BUTTON_STYLE_SQUARE = 6 # type: ButtonStyles
	BUTTON_STYLE_STANDARD = 0 # type: ButtonStyles
	BUTTON_STYLE_TOOL = 7 # type: ButtonStyles

class CalendarTypes :
	CALENDAR_BI_YEARLY = 1 # type: CalendarTypes
	CALENDAR_DEFAULT = 0 # type: CalendarTypes
	CALENDAR_MONTHS = 5 # type: CalendarTypes
	CALENDAR_SEASONS = 4 # type: CalendarTypes
	CALENDAR_TURNS = 3 # type: CalendarTypes
	CALENDAR_WEEKS = 6 # type: CalendarTypes
	CALENDAR_YEARS = 2 # type: CalendarTypes

def CameraFlyingCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class CameraLookAtTypes :
	CAMERALOOKAT_BATTLE = 2 # type: CameraLookAtTypes
	CAMERALOOKAT_BATTLE_ZOOM_IN = 3 # type: CameraLookAtTypes
	CAMERALOOKAT_CITY_ZOOM_IN = 1 # type: CameraLookAtTypes
	CAMERALOOKAT_IMMEDIATE = 5 # type: CameraLookAtTypes
	CAMERALOOKAT_NORMAL = 0 # type: CameraLookAtTypes

class CameraMovementSpeeds :
	CAMERAMOVEMENTSPEED_FAST = 2 # type: CameraMovementSpeeds
	CAMERAMOVEMENTSPEED_NORMAL = 0 # type: CameraMovementSpeeds
	CAMERAMOVEMENTSPEED_SLOW = 1 # type: CameraMovementSpeeds

class CardinalDirectionTypes :
	CARDINALDIRECTION_EAST = 1 # type: CardinalDirectionTypes
	CARDINALDIRECTION_NORTH = 0 # type: CardinalDirectionTypes
	CARDINALDIRECTION_SOUTH = 2 # type: CardinalDirectionTypes
	CARDINALDIRECTION_WEST = 3 # type: CardinalDirectionTypes
	NO_CARDINALDIRECTION = -1 # type: CardinalDirectionTypes
	NUM_CARDINALDIRECTION_TYPES = 4 # type: CardinalDirectionTypes

class ChatTargetTypes :
	CHATTARGET_ALL = -2 # type: ChatTargetTypes
	CHATTARGET_TEAM = -3 # type: ChatTargetTypes
	NO_CHATTARGET = -1 # type: ChatTargetTypes

class CheckBoxStates :
	OFF = 0 # type: CheckBoxStates
	ON = 1 # type: CheckBoxStates

class CitySizeTypes :
	CITYSIZE_LARGE = 2 # type: CitySizeTypes
	CITYSIZE_MEDIUM = 1 # type: CitySizeTypes
	CITYSIZE_SMALL = 0 # type: CitySizeTypes
	NO_CITYSIZE = -1 # type: CitySizeTypes
	NUM_CITYSIZE_TYPES = 3 # type: CitySizeTypes

class CityTabTypes :
	CITYTAB_BUILDINGS = 1 # type: CityTabTypes
	CITYTAB_UNITS = 0 # type: CityTabTypes
	CITYTAB_WONDERS = 2 # type: CityTabTypes
	NUM_CITYTAB_TYPES = 3 # type: CityTabTypes

class CivicOptionTypes :
	NO_CIVICOPTION = -1 # type: CivicOptionTypes

class CivicTypes :
	NO_CIVIC = -1 # type: CivicTypes

class CivilizationTypes :
	NO_CIVILIZATION = -1 # type: CivilizationTypes

class CivilopediaPageTypes :
	CIVILOPEDIA_PAGE_BONUS = 6 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_BUILDING = 2 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_CIV = 11 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_CIVIC = 15 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_CONCEPT = 17 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_CONCEPT_NEW = 18 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_CORPORATION = 14 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_FEATURE = 5 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_HINTS = 19 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_IMPROVEMENT = 7 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_LEADER = 12 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_PROJECT = 16 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_PROMOTION = 9 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_RELIGION = 13 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_SPECIALIST = 8 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_TECH = 0 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_TERRAIN = 4 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_UNIT = 1 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_UNIT_GROUP = 10 # type: CivilopediaPageTypes
	CIVILOPEDIA_PAGE_WONDER = 3 # type: CivilopediaPageTypes
	NO_CIVILOPEDIA_PAGE = -1 # type: CivilopediaPageTypes
	NUM_CIVILOPEDIA_PAGE_TYPES = 20 # type: CivilopediaPageTypes

class ClimateTypes :
	NO_CLIMATE = -1 # type: ClimateTypes

class ColorTypes :
	NO_COLOR = -1 # type: ColorTypes

class CombatDetails( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def eOwner( self ) :
		# type: () -> Any
		pass
	@eOwner.setter
	def eOwner( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def eVisualOwner( self ) :
		# type: () -> Any
		pass
	@eVisualOwner.setter
	def eVisualOwner( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iAIAnimalCombatModifierAA( self ) :
		# type: () -> Any
		pass
	@iAIAnimalCombatModifierAA.setter
	def iAIAnimalCombatModifierAA( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iAIAnimalCombatModifierTA( self ) :
		# type: () -> Any
		pass
	@iAIAnimalCombatModifierTA.setter
	def iAIAnimalCombatModifierTA( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iAIBarbarianCombatModifierAB( self ) :
		# type: () -> Any
		pass
	@iAIBarbarianCombatModifierAB.setter
	def iAIBarbarianCombatModifierAB( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iAIBarbarianCombatModifierTB( self ) :
		# type: () -> Any
		pass
	@iAIBarbarianCombatModifierTB.setter
	def iAIBarbarianCombatModifierTB( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iAmphibAttackModifier( self ) :
		# type: () -> Any
		pass
	@iAmphibAttackModifier.setter
	def iAmphibAttackModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iAnimalCombatModifierA( self ) :
		# type: () -> Any
		pass
	@iAnimalCombatModifierA.setter
	def iAnimalCombatModifierA( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iAnimalCombatModifierAA( self ) :
		# type: () -> Any
		pass
	@iAnimalCombatModifierAA.setter
	def iAnimalCombatModifierAA( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iAnimalCombatModifierT( self ) :
		# type: () -> Any
		pass
	@iAnimalCombatModifierT.setter
	def iAnimalCombatModifierT( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iAnimalCombatModifierTA( self ) :
		# type: () -> Any
		pass
	@iAnimalCombatModifierTA.setter
	def iAnimalCombatModifierTA( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iBarbarianCombatModifierAB( self ) :
		# type: () -> Any
		pass
	@iBarbarianCombatModifierAB.setter
	def iBarbarianCombatModifierAB( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iBarbarianCombatModifierTB( self ) :
		# type: () -> Any
		pass
	@iBarbarianCombatModifierTB.setter
	def iBarbarianCombatModifierTB( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iBaseCombatStr( self ) :
		# type: () -> Any
		pass
	@iBaseCombatStr.setter
	def iBaseCombatStr( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iCityAttackModifier( self ) :
		# type: () -> Any
		pass
	@iCityAttackModifier.setter
	def iCityAttackModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iCityBarbarianDefenseModifier( self ) :
		# type: () -> Any
		pass
	@iCityBarbarianDefenseModifier.setter
	def iCityBarbarianDefenseModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iCityDefenseModifier( self ) :
		# type: () -> Any
		pass
	@iCityDefenseModifier.setter
	def iCityDefenseModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iClassAttackModifier( self ) :
		# type: () -> Any
		pass
	@iClassAttackModifier.setter
	def iClassAttackModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iClassDefenseModifier( self ) :
		# type: () -> Any
		pass
	@iClassDefenseModifier.setter
	def iClassDefenseModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iCombat( self ) :
		# type: () -> Any
		pass
	@iCombat.setter
	def iCombat( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iCombatModifierA( self ) :
		# type: () -> Any
		pass
	@iCombatModifierA.setter
	def iCombatModifierA( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iCombatModifierT( self ) :
		# type: () -> Any
		pass
	@iCombatModifierT.setter
	def iCombatModifierT( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iCurrCombatStr( self ) :
		# type: () -> Any
		pass
	@iCurrCombatStr.setter
	def iCurrCombatStr( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iCurrHitPoints( self ) :
		# type: () -> Any
		pass
	@iCurrHitPoints.setter
	def iCurrHitPoints( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iDomainDefenseModifier( self ) :
		# type: () -> Any
		pass
	@iDomainDefenseModifier.setter
	def iDomainDefenseModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iDomainModifierA( self ) :
		# type: () -> Any
		pass
	@iDomainModifierA.setter
	def iDomainModifierA( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iDomainModifierT( self ) :
		# type: () -> Any
		pass
	@iDomainModifierT.setter
	def iDomainModifierT( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iExtraCombatPercent( self ) :
		# type: () -> Any
		pass
	@iExtraCombatPercent.setter
	def iExtraCombatPercent( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iFeatureAttackModifier( self ) :
		# type: () -> Any
		pass
	@iFeatureAttackModifier.setter
	def iFeatureAttackModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iFeatureDefenseModifier( self ) :
		# type: () -> Any
		pass
	@iFeatureDefenseModifier.setter
	def iFeatureDefenseModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iFortifyModifier( self ) :
		# type: () -> Any
		pass
	@iFortifyModifier.setter
	def iFortifyModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iHillsAttackModifier( self ) :
		# type: () -> Any
		pass
	@iHillsAttackModifier.setter
	def iHillsAttackModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iHillsDefenseModifier( self ) :
		# type: () -> Any
		pass
	@iHillsDefenseModifier.setter
	def iHillsDefenseModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iKamikazeModifier( self ) :
		# type: () -> Any
		pass
	@iKamikazeModifier.setter
	def iKamikazeModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iMaxCombatStr( self ) :
		# type: () -> Any
		pass
	@iMaxCombatStr.setter
	def iMaxCombatStr( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iMaxHitPoints( self ) :
		# type: () -> Any
		pass
	@iMaxHitPoints.setter
	def iMaxHitPoints( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iModifierTotal( self ) :
		# type: () -> Any
		pass
	@iModifierTotal.setter
	def iModifierTotal( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iPlotDefenseModifier( self ) :
		# type: () -> Any
		pass
	@iPlotDefenseModifier.setter
	def iPlotDefenseModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iRiverAttackModifier( self ) :
		# type: () -> Any
		pass
	@iRiverAttackModifier.setter
	def iRiverAttackModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iTerrainAttackModifier( self ) :
		# type: () -> Any
		pass
	@iTerrainAttackModifier.setter
	def iTerrainAttackModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iTerrainDefenseModifier( self ) :
		# type: () -> Any
		pass
	@iTerrainDefenseModifier.setter
	def iTerrainDefenseModifier( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def sUnitName( self ) :
		# type: () -> Any
		pass
	@sUnitName.setter
	def sUnitName( self, value ) :
		# type: (Any) -> None
		pass

class CommandTypes :
	COMMAND_AUTOMATE = 2 # type: CommandTypes
	COMMAND_CANCEL = 4 # type: CommandTypes
	COMMAND_CANCEL_ALL = 5 # type: CommandTypes
	COMMAND_DELETE = 7 # type: CommandTypes
	COMMAND_GIFT = 8 # type: CommandTypes
	COMMAND_HOTKEY = 13 # type: CommandTypes
	COMMAND_LOAD = 9 # type: CommandTypes
	COMMAND_LOAD_UNIT = 10 # type: CommandTypes
	COMMAND_PROMOTION = 0 # type: CommandTypes
	COMMAND_STOP_AUTOMATION = 6 # type: CommandTypes
	COMMAND_UNLOAD = 11 # type: CommandTypes
	COMMAND_UNLOAD_ALL = 12 # type: CommandTypes
	COMMAND_UPGRADE = 1 # type: CommandTypes
	COMMAND_WAKE = 3 # type: CommandTypes
	NO_COMMAND = -1 # type: CommandTypes
	NUM_COMMAND_TYPES = 14 # type: CommandTypes

class CommerceTypes :
	COMMERCE_CULTURE = 2 # type: CommerceTypes
	COMMERCE_ESPIONAGE = 3 # type: CommerceTypes
	COMMERCE_GOLD = 0 # type: CommerceTypes
	COMMERCE_RESEARCH = 1 # type: CommerceTypes
	NUM_COMMERCE_TYPES = 4 # type: CommerceTypes

class ConceptTypes :
	NO_CONCEPT = -1 # type: ConceptTypes

class ContactTypes :
	CONTACT_ASK_FOR_HELP = 5 # type: ContactTypes
	CONTACT_CIVIC_PRESSURE = 1 # type: ContactTypes
	CONTACT_DEFENSIVE_PACT = 8 # type: ContactTypes
	CONTACT_DEMAND_TRIBUTE = 6 # type: ContactTypes
	CONTACT_GIVE_HELP = 4 # type: ContactTypes
	CONTACT_JOIN_WAR = 2 # type: ContactTypes
	CONTACT_OPEN_BORDERS = 7 # type: ContactTypes
	CONTACT_PEACE_TREATY = 10 # type: ContactTypes
	CONTACT_PERMANENT_ALLIANCE = 9 # type: ContactTypes
	CONTACT_RELIGION_PRESSURE = 0 # type: ContactTypes
	CONTACT_STOP_TRADING = 3 # type: ContactTypes
	CONTACT_TRADE_BONUS = 12 # type: ContactTypes
	CONTACT_TRADE_MAP = 13 # type: ContactTypes
	CONTACT_TRADE_TECH = 11 # type: ContactTypes
	NUM_CONTACT_TYPES = 14 # type: ContactTypes

class ControlTypes :
	CONTROL_ADMIN_DETAILS = 56 # type: ControlTypes
	CONTROL_AUTOMOVES = 16 # type: ControlTypes
	CONTROL_BARE_MAP = 20 # type: ControlTypes
	CONTROL_CENTERONSELECTION = 0 # type: ControlTypes
	CONTROL_CHAT_ALL = 49 # type: ControlTypes
	CONTROL_CHAT_TEAM = 50 # type: ControlTypes
	CONTROL_CIVICS_SCREEN = 43 # type: ControlTypes
	CONTROL_CIVILOPEDIA = 40 # type: ControlTypes
	CONTROL_CORPORATION_SCREEN = 42 # type: ControlTypes
	CONTROL_CYCLEUNIT = 9 # type: ControlTypes
	CONTROL_CYCLEUNIT_ALT = 10 # type: ControlTypes
	CONTROL_CYCLEWORKER = 11 # type: ControlTypes
	CONTROL_CYCLE_CAMERA_FLYING_MODES = 34 # type: ControlTypes
	CONTROL_DETAILS = 55 # type: ControlTypes
	CONTROL_DIPLOMACY = 59 # type: ControlTypes
	CONTROL_DOMESTIC_SCREEN = 51 # type: ControlTypes
	CONTROL_ENDTURN = 13 # type: ControlTypes
	CONTROL_ENDTURN_ALT = 14 # type: ControlTypes
	CONTROL_ESPIONAGE_SCREEN = 61 # type: ControlTypes
	CONTROL_FINANCIAL_SCREEN = 45 # type: ControlTypes
	CONTROL_FLYING_CAMERA = 37 # type: ControlTypes
	CONTROL_FORCEENDTURN = 15 # type: ControlTypes
	CONTROL_FOREIGN_SCREEN = 44 # type: ControlTypes
	CONTROL_FREE_COLONY = 62 # type: ControlTypes
	CONTROL_GLOBELAYER = 24 # type: ControlTypes
	CONTROL_GLOBE_VIEW = 54 # type: ControlTypes
	CONTROL_GRID = 19 # type: ControlTypes
	CONTROL_HALL_OF_FAME = 57 # type: ControlTypes
	CONTROL_INFO = 53 # type: ControlTypes
	CONTROL_ISOMETRIC_CAMERA_LEFT = 35 # type: ControlTypes
	CONTROL_ISOMETRIC_CAMERA_RIGHT = 36 # type: ControlTypes
	CONTROL_LASTUNIT = 12 # type: ControlTypes
	CONTROL_LOAD_GAME = 26 # type: ControlTypes
	CONTROL_MILITARY_SCREEN = 46 # type: ControlTypes
	CONTROL_MOUSE_FLYING_CAMERA = 38 # type: ControlTypes
	CONTROL_NEXTCITY = 5 # type: ControlTypes
	CONTROL_NEXTUNIT = 7 # type: ControlTypes
	CONTROL_OPTIONS_SCREEN = 27 # type: ControlTypes
	CONTROL_ORTHO_CAMERA = 33 # type: ControlTypes
	CONTROL_PING = 17 # type: ControlTypes
	CONTROL_PREVCITY = 6 # type: ControlTypes
	CONTROL_PREVUNIT = 8 # type: ControlTypes
	CONTROL_QUICK_LOAD = 32 # type: ControlTypes
	CONTROL_QUICK_SAVE = 31 # type: ControlTypes
	CONTROL_RELIGION_SCREEN = 41 # type: ControlTypes
	CONTROL_RESOURCE_ALL = 22 # type: ControlTypes
	CONTROL_RETIRE = 28 # type: ControlTypes
	CONTROL_SAVE_GROUP = 29 # type: ControlTypes
	CONTROL_SAVE_NORMAL = 30 # type: ControlTypes
	CONTROL_SCORES = 25 # type: ControlTypes
	CONTROL_SELECTCAPITAL = 4 # type: ControlTypes
	CONTROL_SELECTCITY = 3 # type: ControlTypes
	CONTROL_SELECTYUNITALL = 2 # type: ControlTypes
	CONTROL_SELECTYUNITTYPE = 1 # type: ControlTypes
	CONTROL_SELECT_HEALTHY = 60 # type: ControlTypes
	CONTROL_SIGN = 18 # type: ControlTypes
	CONTROL_TECH_CHOOSER = 47 # type: ControlTypes
	CONTROL_TOP_DOWN_CAMERA = 39 # type: ControlTypes
	CONTROL_TURN_LOG = 48 # type: ControlTypes
	CONTROL_UNIT_ICONS = 23 # type: ControlTypes
	CONTROL_VICTORY_SCREEN = 52 # type: ControlTypes
	CONTROL_WORLD_BUILDER = 58 # type: ControlTypes
	CONTROL_YIELDS = 21 # type: ControlTypes
	NO_CONTROL = -1 # type: ControlTypes
	NUM_CONTROL_TYPES = 63 # type: ControlTypes

class CorporationTypes :
	NO_CORPORATION = -1 # type: CorporationTypes

class CultureLevelTypes :
	NO_CULTURELEVEL = -1 # type: CultureLevelTypes

class CursorTypes :
	NO_CURSOR = -1 # type: CursorTypes

class CustomMapOptionTypes :
	NO_CUSTOM_MAPOPTION = -1 # type: CustomMapOptionTypes

def CutTreesCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class CvActionInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAutomateType( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCommandData( self ) :
		# type: () -> int
		pass
	def getCommandType( self ) :
		# type: () -> int
		pass
	def getControlType( self ) :
		# type: () -> int
		pass
	def getHotKey( self ) :
		# type: () -> str
		pass
	def getInterfaceModeType( self ) :
		# type: () -> int
		pass
	def getMissionData( self ) :
		# type: () -> int
		pass
	def getMissionType( self ) :
		# type: () -> int
		pass
	def isConfirmCommand( self ) :
		# type: () -> bool
		pass
	def isVisible( self ) :
		# type: () -> bool
		pass

class CvArtInfoAsset( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoBonus( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoBuilding( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def isAnimated( self ) :
		# type: () -> bool
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoCivilization( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def isWhiteFlag( self ) :
		# type: () -> bool
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoFeature( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getFeatureDummyNodeName( self, arg0, arg1 ) :
		# type: (int, str) -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def isAnimated( self ) :
		# type: () -> bool
		pass
	def isRiverArt( self ) :
		# type: () -> bool
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoImprovement( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def isExtraAnimations( self ) :
		# type: () -> bool
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoInterface( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoLeaderhead( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoMisc( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoMovie( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoScalableAsset( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoTerrain( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvArtInfoUnit( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getInterfaceScale( self ) :
		# type: () -> float
		pass
	def getKFM( self ) :
		# type: () -> str
		pass
	def getNIF( self ) :
		# type: () -> str
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def setKFM( self, arg0 ) :
		# type: (str) -> None
		pass
	def setNIF( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvAssetInfoBase( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getTag( self ) :
		# type: () -> str
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setTag( self, arg0 ) :
		# type: (str) -> None
		pass

class CvAutomateInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvBonusClassInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUniqueRange( self, *args, **kwargs ) :
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvBonusInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAIObjective( self ) :
		# type: () -> int
		pass
	def getAITradeModifier( self ) :
		# type: () -> int
		pass
	def getArtDefineTag( self ) :
		# type: () -> str
		pass
	def getArtInfo( self ) :
		# type: () -> CvArtInfoBonus
		pass
	def getBonusClassType( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getChar( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getConstAppearance( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getGroupRand( self ) :
		# type: () -> int
		pass
	def getGroupRange( self ) :
		# type: () -> int
		pass
	def getHappiness( self ) :
		# type: () -> int
		pass
	def getHealth( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getMaxLatitude( self ) :
		# type: () -> int
		pass
	def getMinAreaSize( self ) :
		# type: () -> int
		pass
	def getMinLandPercent( self ) :
		# type: () -> int
		pass
	def getMinLatitude( self ) :
		# type: () -> int
		pass
	def getPercentPerPlayer( self ) :
		# type: () -> int
		pass
	def getPlacementOrder( self ) :
		# type: () -> int
		pass
	def getRandAppearance1( self ) :
		# type: () -> int
		pass
	def getRandAppearance2( self ) :
		# type: () -> int
		pass
	def getRandAppearance3( self ) :
		# type: () -> int
		pass
	def getRandAppearance4( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechCityTrade( self ) :
		# type: () -> int
		pass
	def getTechObsolete( self ) :
		# type: () -> int
		pass
	def getTechReveal( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTilesPer( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUniqueRange( self ) :
		# type: () -> int
		pass
	def getYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def isFeature( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isFeatureTerrain( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isFlatlands( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isHills( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isNoRiverSide( self ) :
		# type: () -> bool
		pass
	def isNormalize( self ) :
		# type: () -> bool
		pass
	def isOneArea( self ) :
		# type: () -> bool
		pass
	def isTerrain( self, arg0 ) :
		# type: (int) -> bool
		pass

class CvBuildInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCost( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getEntityEvent( self ) :
		# type: () -> int
		pass
	def getFeatureProduction( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFeatureTech( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFeatureTime( self, arg0 ) :
		# type: (int) -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getImprovement( self ) :
		# type: () -> int
		pass
	def getMissionType( self ) :
		# type: () -> int
		pass
	def getRoute( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechPrereq( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTime( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isFeatureRemove( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isKill( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvBuildingClassInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefaultBuildingIndex( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getExtraPlayerInstances( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getMaxGlobalInstances( self ) :
		# type: () -> int
		pass
	def getMaxPlayerInstances( self ) :
		# type: () -> int
		pass
	def getMaxTeamInstances( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getVictoryThreshold( self, arg0 ) :
		# type: (int) -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isMonument( self ) :
		# type: () -> bool
		pass
	def isNoLimit( self ) :
		# type: () -> bool
		pass

class CvBuildingInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAIWeight( self ) :
		# type: () -> int
		pass
	def getAdvisorType( self ) :
		# type: () -> int
		pass
	def getAirModifier( self ) :
		# type: () -> int
		pass
	def getAirUnitCapacity( self ) :
		# type: () -> int
		pass
	def getAirlift( self ) :
		# type: () -> int
		pass
	def getAllCityDefenseModifier( self ) :
		# type: () -> int
		pass
	def getAnarchyModifier( self ) :
		# type: () -> int
		pass
	def getAreaFreeSpecialist( self ) :
		# type: () -> int
		pass
	def getAreaHappiness( self ) :
		# type: () -> int
		pass
	def getAreaHealth( self ) :
		# type: () -> int
		pass
	def getArtDefineTag( self ) :
		# type: () -> str
		pass
	def getArtInfo( self, *args, **kwargs ) :
		pass
	def getAssetValue( self ) :
		# type: () -> int
		pass
	def getBombardDefenseModifier( self ) :
		# type: () -> int
		pass
	def getBonusHappinessChanges( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBonusHealthChanges( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBonusProductionModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBonusYieldModifier( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getBuildingClassType( self ) :
		# type: () -> int
		pass
	def getBuildingHappinessChanges( self, arg0 ) :
		# type: (int) -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivic( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCoastalTradeRoutes( self ) :
		# type: () -> int
		pass
	def getCommerceChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCommerceChangeDoubleTime( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCommerceHappiness( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCommerceModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getConquestProbability( self ) :
		# type: () -> int
		pass
	def getConstructSound( self ) :
		# type: () -> str
		pass
	def getDefenseModifier( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDomainFreeExperience( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDomainProductionModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDomesticGreatGeneralRateModifier( self ) :
		# type: () -> int
		pass
	def getEnemyWarWearinessModifier( self ) :
		# type: () -> int
		pass
	def getEspionageDefenseModifier( self ) :
		# type: () -> int
		pass
	def getFlavorValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFoodKept( self ) :
		# type: () -> int
		pass
	def getForeignTradeRouteModifier( self ) :
		# type: () -> int
		pass
	def getFoundsCorporation( self ) :
		# type: () -> int
		pass
	def getFreeBonus( self ) :
		# type: () -> int
		pass
	def getFreeBuildingClass( self ) :
		# type: () -> int
		pass
	def getFreeExperience( self ) :
		# type: () -> int
		pass
	def getFreePromotion( self ) :
		# type: () -> int
		pass
	def getFreeSpecialist( self ) :
		# type: () -> int
		pass
	def getFreeSpecialistCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFreeStartEra( self ) :
		# type: () -> int
		pass
	def getFreeTechs( self ) :
		# type: () -> int
		pass
	def getGlobalCommerceModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getGlobalCorporationCommerce( self ) :
		# type: () -> int
		pass
	def getGlobalFreeExperience( self ) :
		# type: () -> int
		pass
	def getGlobalFreeSpecialist( self ) :
		# type: () -> int
		pass
	def getGlobalGreatPeopleRateModifier( self ) :
		# type: () -> int
		pass
	def getGlobalHappiness( self ) :
		# type: () -> int
		pass
	def getGlobalHealth( self ) :
		# type: () -> int
		pass
	def getGlobalHurryModifier( self ) :
		# type: () -> int
		pass
	def getGlobalPopulationChange( self ) :
		# type: () -> int
		pass
	def getGlobalReligionCommerce( self ) :
		# type: () -> int
		pass
	def getGlobalSeaPlotYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getGlobalSpaceProductionModifier( self ) :
		# type: () -> int
		pass
	def getGlobalTradeRoutes( self ) :
		# type: () -> int
		pass
	def getGlobalWarWearinessModifier( self ) :
		# type: () -> int
		pass
	def getGlobalYieldModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getGoldenAgeModifier( self ) :
		# type: () -> int
		pass
	def getGreatGeneralRateModifier( self ) :
		# type: () -> int
		pass
	def getGreatPeopleRateChange( self ) :
		# type: () -> int
		pass
	def getGreatPeopleRateModifier( self ) :
		# type: () -> int
		pass
	def getGreatPeopleUnitClass( self ) :
		# type: () -> int
		pass
	def getHappiness( self ) :
		# type: () -> int
		pass
	def getHappinessTraits( self, arg0 ) :
		# type: (int) -> int
		pass
	def getHealRateChange( self ) :
		# type: () -> int
		pass
	def getHealth( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHolyCity( self ) :
		# type: () -> int
		pass
	def getHotKey( self ) :
		# type: () -> str
		pass
	def getHotKeyDescription( self ) :
		# type: () -> str
		pass
	def getHurryAngerModifier( self ) :
		# type: () -> int
		pass
	def getHurryCostModifier( self ) :
		# type: () -> int
		pass
	def getImprovementFreeSpecialist( self, arg0 ) :
		# type: (int) -> int
		pass
	def getMaintenanceModifier( self ) :
		# type: () -> int
		pass
	def getMaxLatitude( self ) :
		# type: () -> int
		pass
	def getMaxStartEra( self ) :
		# type: () -> int
		pass
	def getMilitaryProductionModifier( self ) :
		# type: () -> int
		pass
	def getMinAreaSize( self ) :
		# type: () -> int
		pass
	def getMinLatitude( self ) :
		# type: () -> int
		pass
	def getMissionType( self ) :
		# type: () -> int
		pass
	def getMovie( self ) :
		# type: () -> str
		pass
	def getMovieDefineTag( self ) :
		# type: () -> str
		pass
	def getNoBonus( self ) :
		# type: () -> int
		pass
	def getNukeExplosionRand( self ) :
		# type: () -> int
		pass
	def getNukeModifier( self ) :
		# type: () -> int
		pass
	def getNumCitiesPrereq( self ) :
		# type: () -> int
		pass
	def getNumFreeBonuses( self ) :
		# type: () -> int
		pass
	def getNumTeamsPrereq( self ) :
		# type: () -> int
		pass
	def getObsoleteSafeCommerceChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getObsoleteTech( self ) :
		# type: () -> int
		pass
	def getPowerBonus( self ) :
		# type: () -> int
		pass
	def getPowerValue( self ) :
		# type: () -> int
		pass
	def getPowerYieldModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPrereqAndBonus( self ) :
		# type: () -> int
		pass
	def getPrereqAndTech( self ) :
		# type: () -> int
		pass
	def getPrereqAndTechs( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPrereqCorporation( self ) :
		# type: () -> int
		pass
	def getPrereqNumOfBuildingClass( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPrereqOrBonuses( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPrereqReligion( self ) :
		# type: () -> int
		pass
	def getProductionCost( self ) :
		# type: () -> int
		pass
	def getProductionTraits( self, arg0 ) :
		# type: (int) -> int
		pass
	def getReligionChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getReligionType( self ) :
		# type: () -> int
		pass
	def getRiverPlotYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def getSeaPlotYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSpaceProductionModifier( self ) :
		# type: () -> int
		pass
	def getSpecialBuildingType( self ) :
		# type: () -> int
		pass
	def getSpecialistCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSpecialistYieldChange( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getStateReligion( self ) :
		# type: () -> int
		pass
	def getStateReligionCommerce( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStateReligionHappiness( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTradeRouteModifier( self ) :
		# type: () -> int
		pass
	def getTradeRoutes( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnitCombatFreeExperience( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitLevelPrereq( self ) :
		# type: () -> int
		pass
	def getVictoryPrereq( self ) :
		# type: () -> int
		pass
	def getVoteSourceType( self ) :
		# type: () -> int
		pass
	def getWarWearinessModifier( self ) :
		# type: () -> int
		pass
	def getWorkerSpeedModifier( self ) :
		# type: () -> int
		pass
	def getYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getYieldModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def isAllowsNukes( self ) :
		# type: () -> bool
		pass
	def isAreaBorderObstacle( self ) :
		# type: () -> bool
		pass
	def isAreaCleanPower( self ) :
		# type: () -> bool
		pass
	def isBuildingClassNeededInCity( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isBuildingOnlyHealthy( self ) :
		# type: () -> bool
		pass
	def isCapital( self ) :
		# type: () -> bool
		pass
	def isCenterInCity( self ) :
		# type: () -> bool
		pass
	def isCommerceChangeOriginalOwner( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isCommerceFlexible( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isDirtyPower( self ) :
		# type: () -> bool
		pass
	def isForceTeamVoteEligible( self ) :
		# type: () -> bool
		pass
	def isGoldenAge( self ) :
		# type: () -> bool
		pass
	def isGovernmentCenter( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMapCentering( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isNeverCapture( self ) :
		# type: () -> bool
		pass
	def isNoUnhappiness( self ) :
		# type: () -> bool
		pass
	def isNoUnhealthyPopulation( self ) :
		# type: () -> bool
		pass
	def isNukeImmune( self ) :
		# type: () -> bool
		pass
	def isPower( self ) :
		# type: () -> bool
		pass
	def isPrereqReligion( self ) :
		# type: () -> bool
		pass
	def isRiver( self ) :
		# type: () -> bool
		pass
	def isStateReligion( self ) :
		# type: () -> bool
		pass
	def isTeamShare( self ) :
		# type: () -> bool
		pass
	def isWater( self ) :
		# type: () -> bool
		pass
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass

class CvCivicInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAIWeight( self ) :
		# type: () -> int
		pass
	def getAnarchyLength( self ) :
		# type: () -> int
		pass
	def getBaseFreeMilitaryUnits( self ) :
		# type: () -> int
		pass
	def getBaseFreeUnits( self ) :
		# type: () -> int
		pass
	def getBuildingHappinessChanges( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingHealthChanges( self, arg0 ) :
		# type: (int) -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCapitalCommerceModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCapitalYieldModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCivicOptionType( self ) :
		# type: () -> int
		pass
	def getCivicPercentAnger( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCommerceModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCorporationMaintenanceModifier( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDistanceMaintenanceModifier( self ) :
		# type: () -> int
		pass
	def getDomesticGreatGeneralRateModifier( self ) :
		# type: () -> int
		pass
	def getExpInBorderModifier( self ) :
		# type: () -> bool
		pass
	def getExtraHealth( self ) :
		# type: () -> int
		pass
	def getFeatureHappinessChanges( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFreeExperience( self ) :
		# type: () -> int
		pass
	def getFreeMilitaryUnitsPopulationPercent( self ) :
		# type: () -> int
		pass
	def getFreeSpecialist( self ) :
		# type: () -> int
		pass
	def getFreeUnitsPopulationPercent( self ) :
		# type: () -> int
		pass
	def getGoldPerMilitaryUnit( self ) :
		# type: () -> int
		pass
	def getGoldPerUnit( self ) :
		# type: () -> int
		pass
	def getGreatGeneralRateModifier( self ) :
		# type: () -> int
		pass
	def getGreatPeopleRateModifier( self ) :
		# type: () -> int
		pass
	def getHappyPerMilitaryUnit( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getImprovementUpgradeRateModifier( self ) :
		# type: () -> int
		pass
	def getImprovementYieldChanges( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getLargestCityHappiness( self ) :
		# type: () -> int
		pass
	def getMaxConscript( self ) :
		# type: () -> int
		pass
	def getMilitaryProductionModifier( self ) :
		# type: () -> int
		pass
	def getNonStateReligionHappiness( self ) :
		# type: () -> int
		pass
	def getNumCitiesMaintenanceModifier( self ) :
		# type: () -> int
		pass
	def getSpecialistExtraCommerce( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStateReligionBuildingProductionModifier( self ) :
		# type: () -> int
		pass
	def getStateReligionFreeExperience( self ) :
		# type: () -> int
		pass
	def getStateReligionGreatPeopleRateModifier( self ) :
		# type: () -> int
		pass
	def getStateReligionHappiness( self ) :
		# type: () -> int
		pass
	def getStateReligionUnitProductionModifier( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechPrereq( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTradeRoutes( self ) :
		# type: () -> int
		pass
	def getTradeYieldModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUpkeep( self ) :
		# type: () -> int
		pass
	def getWarWearinessModifier( self ) :
		# type: () -> int
		pass
	def getWorkerSpeedModifier( self ) :
		# type: () -> int
		pass
	def getYieldModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def isBuildingOnlyHealthy( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isHurry( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isMilitaryFoodProduction( self ) :
		# type: () -> bool
		pass
	def isNoCorporations( self ) :
		# type: () -> bool
		pass
	def isNoForeignCorporations( self ) :
		# type: () -> bool
		pass
	def isNoForeignTrade( self ) :
		# type: () -> bool
		pass
	def isNoNonStateReligionSpread( self ) :
		# type: () -> bool
		pass
	def isNoUnhealthyPopulation( self ) :
		# type: () -> bool
		pass
	def isSpecialBuildingNotRequired( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isSpecialistValid( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isStateReligion( self ) :
		# type: () -> bool
		pass
	def pyGetWeLoveTheKing( self ) :
		# type: () -> unicode
		pass

class CvCivicOptionInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTraitNoUpkeep( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvCivilizationInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getActionSoundScriptId( self, *args, **kwargs ) :
		pass
	def getAdjective( self ) :
		# type: () -> unicode
		pass
	def getArtDefineTag( self ) :
		# type: () -> str
		pass
	def getArtStyleType( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCityNames( self, arg0 ) :
		# type: (int) -> str
		pass
	def getCivilizationBuildings( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCivilizationFreeUnitsClass( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCivilizationInitialCivics( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCivilizationUnits( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefaultPlayerColor( self ) :
		# type: () -> int
		pass
	def getDerivativeCiv( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getFlagTexture( self ) :
		# type: () -> str
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getNumCityNames( self ) :
		# type: () -> int
		pass
	def getNumLeaders( self ) :
		# type: () -> int
		pass
	def getSelectionSoundScriptId( self, *args, **kwargs ) :
		pass
	def getShortDescription( self ) :
		# type: () -> unicode
		pass
	def getShortDescriptionKey( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isAIPlayable( self ) :
		# type: () -> bool
		pass
	def isCivilizationDisableTechs( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isCivilizationFreeBuildingClass( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isCivilizationFreeTechs( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isLeaders( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isPlayable( self ) :
		# type: () -> bool
		pass

class CvClimateInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDesertBottomLatitudeChange( self ) :
		# type: () -> float
		pass
	def getDesertPercentChange( self ) :
		# type: () -> int
		pass
	def getDesertTopLatitudeChange( self ) :
		# type: () -> float
		pass
	def getGrassLatitudeChange( self ) :
		# type: () -> float
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHillRange( self ) :
		# type: () -> int
		pass
	def getIceLatitude( self ) :
		# type: () -> float
		pass
	def getJungleLatitude( self ) :
		# type: () -> int
		pass
	def getPeakPercent( self ) :
		# type: () -> int
		pass
	def getRandIceLatitude( self ) :
		# type: () -> float
		pass
	def getSnowLatitudeChange( self ) :
		# type: () -> float
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTundraLatitudeChange( self ) :
		# type: () -> float
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvColorInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getColor( self, *args, **kwargs ) :
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvCommandInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvCommerceInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAIWeightPercent( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getChar( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getInitialHappiness( self ) :
		# type: () -> int
		pass
	def getInitialPercent( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isFlexiblePercent( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvControlInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getActionInfoIndex( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvCorporationInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getChar( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCommerceProduced( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getFreeUnitClass( self ) :
		# type: () -> int
		pass
	def getHeadquarterChar( self ) :
		# type: () -> int
		pass
	def getHeadquarterCommerce( self, arg0 ) :
		# type: (int) -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getMaintenance( self ) :
		# type: () -> int
		pass
	def getMissionType( self ) :
		# type: () -> int
		pass
	def getMovieFile( self ) :
		# type: () -> str
		pass
	def getMovieSound( self ) :
		# type: () -> str
		pass
	def getPrereqBonus( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSound( self ) :
		# type: () -> str
		pass
	def getSpreadCost( self ) :
		# type: () -> int
		pass
	def getSpreadFactor( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechPrereq( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getYieldProduced( self, arg0 ) :
		# type: (int) -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvCultureLevelInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCityDefenseModifier( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getSpeedThreshold( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvDiplomacyInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAttitudeTypes( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilizationTypes( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDiplomacyPowerTypes( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def getDiplomacyText( self, arg0, arg1 ) :
		# type: (int, int) -> str
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getLeaderHeadTypes( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def getNumDiplomacyText( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNumResponses( self ) :
		# type: () -> int
		pass
	def getResponse( self, arg0 ) :
		# type: (int) -> CvDiplomacyResponse
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvDiplomacyTextInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAttitudeTypes( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilizationTypes( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDiplomacyPowerTypes( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def getDiplomacyText( self, arg0, arg1 ) :
		# type: (int, int) -> str
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getLeaderHeadTypes( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def getNumDiplomacyText( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNumResponses( self ) :
		# type: () -> int
		pass
	def getResponse( self, arg0 ) :
		# type: (int) -> Response
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvEffectInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getPath( self ) :
		# type: () -> str
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def setPath( self, arg0 ) :
		# type: (str) -> None
		pass
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass

class CvEmphasizeInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCommerceChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def isAvoidGrowth( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isGreatPeople( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvEraInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAnarchyPercent( self ) :
		# type: () -> int
		pass
	def getAudioUnitDefeatScript( self ) :
		# type: () -> str
		pass
	def getAudioUnitVictoryScript( self ) :
		# type: () -> str
		pass
	def getBuildPercent( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCitySoundscapeSciptId( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getConstructPercent( self ) :
		# type: () -> int
		pass
	def getCreatePercent( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getEventChancePerTurn( self ) :
		# type: () -> int
		pass
	def getFreePopulation( self ) :
		# type: () -> int
		pass
	def getGreatPeoplePercent( self ) :
		# type: () -> int
		pass
	def getGrowthPercent( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getImprovementPercent( self ) :
		# type: () -> int
		pass
	def getNumSoundtracks( self ) :
		# type: () -> int
		pass
	def getResearchPercent( self ) :
		# type: () -> int
		pass
	def getSoundtrackSpace( self ) :
		# type: () -> int
		pass
	def getSoundtracks( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStartPercent( self ) :
		# type: () -> int
		pass
	def getStartingDefenseUnits( self ) :
		# type: () -> int
		pass
	def getStartingExploreUnits( self ) :
		# type: () -> int
		pass
	def getStartingGold( self ) :
		# type: () -> int
		pass
	def getStartingUnitMultiplier( self ) :
		# type: () -> int
		pass
	def getStartingWorkerUnits( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTrainPercent( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isFirstSoundtrackFirst( self ) :
		# type: () -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isNoAnimals( self ) :
		# type: () -> bool
		pass
	def isNoBarbCities( self ) :
		# type: () -> bool
		pass
	def isNoBarbUnits( self ) :
		# type: () -> bool
		pass
	def isNoGoodies( self ) :
		# type: () -> bool
		pass

class CvEspionageMissionInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getBuyCityCostFactor( self ) :
		# type: () -> int
		pass
	def getBuyTechCostFactor( self ) :
		# type: () -> int
		pass
	def getBuyUnitCostFactor( self ) :
		# type: () -> int
		pass
	def getCityInsertCultureAmountFactor( self ) :
		# type: () -> int
		pass
	def getCityInsertCultureCostFactor( self ) :
		# type: () -> int
		pass
	def getCityPoisonWaterCounter( self ) :
		# type: () -> int
		pass
	def getCityRevoltCounter( self ) :
		# type: () -> int
		pass
	def getCityUnhappinessCounter( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCost( self ) :
		# type: () -> int
		pass
	def getCounterespionageMod( self ) :
		# type: () -> int
		pass
	def getCounterespionageNumTurns( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDestroyBuildingCostFactor( self ) :
		# type: () -> int
		pass
	def getDestroyUnitCostFactor( self ) :
		# type: () -> int
		pass
	def getDifficultyMod( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getPlayerAnarchyCounter( self ) :
		# type: () -> int
		pass
	def getStealTreasuryTypes( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getSwitchCivicCostFactor( self ) :
		# type: () -> int
		pass
	def getSwitchReligionCostFactor( self ) :
		# type: () -> int
		pass
	def getTechPrereq( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getVisibilityLevel( self ) :
		# type: () -> int
		pass
	def isDestroyImprovement( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isInvestigateCity( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isNoActiveMissions( self ) :
		# type: () -> bool
		pass
	def isPassive( self ) :
		# type: () -> bool
		pass
	def isSeeDemographics( self ) :
		# type: () -> bool
		pass
	def isSeeResearch( self ) :
		# type: () -> bool
		pass
	def isSelectPlot( self ) :
		# type: () -> bool
		pass
	def isTargetsCity( self ) :
		# type: () -> bool
		pass
	def isTwoPhases( self ) :
		# type: () -> bool
		pass

class CvEventInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAIValue( self ) :
		# type: () -> int
		pass
	def getAdditionalEventChance( self, arg0 ) :
		# type: (int) -> int
		pass
	def getAdditionalEventTime( self, arg0 ) :
		# type: (int) -> int
		pass
	def getAttitudeModifier( self ) :
		# type: () -> int
		pass
	def getBonus( self ) :
		# type: () -> int
		pass
	def getBonusChange( self ) :
		# type: () -> int
		pass
	def getBonusGift( self ) :
		# type: () -> int
		pass
	def getBonusRevealed( self ) :
		# type: () -> int
		pass
	def getBuildingChange( self ) :
		# type: () -> int
		pass
	def getBuildingClass( self ) :
		# type: () -> int
		pass
	def getBuildingCommerceChange( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getBuildingHappyChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingHealthChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingYieldChange( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getClearEventChance( self, arg0 ) :
		# type: (int) -> int
		pass
	def getConvertOtherCities( self ) :
		# type: () -> int
		pass
	def getConvertOwnCities( self ) :
		# type: () -> int
		pass
	def getCulture( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getEspionagePoints( self ) :
		# type: () -> int
		pass
	def getFeature( self ) :
		# type: () -> int
		pass
	def getFeatureChange( self ) :
		# type: () -> int
		pass
	def getFood( self ) :
		# type: () -> int
		pass
	def getFoodPercent( self ) :
		# type: () -> int
		pass
	def getFreeSpecialistCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFreeUnitSupport( self ) :
		# type: () -> int
		pass
	def getGold( self ) :
		# type: () -> int
		pass
	def getHappy( self ) :
		# type: () -> int
		pass
	def getHappyTurns( self ) :
		# type: () -> int
		pass
	def getHealth( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHurryAnger( self ) :
		# type: () -> int
		pass
	def getImprovement( self ) :
		# type: () -> int
		pass
	def getImprovementChange( self ) :
		# type: () -> int
		pass
	def getInflationModifier( self ) :
		# type: () -> int
		pass
	def getMaxNumReligions( self ) :
		# type: () -> int
		pass
	def getMaxPillage( self ) :
		# type: () -> int
		pass
	def getMinPillage( self ) :
		# type: () -> int
		pass
	def getNumBuildingCommerceChanges( self ) :
		# type: () -> int
		pass
	def getNumBuildingHappyChanges( self ) :
		# type: () -> int
		pass
	def getNumBuildingHealthChanges( self ) :
		# type: () -> int
		pass
	def getNumBuildingYieldChanges( self ) :
		# type: () -> int
		pass
	def getNumUnits( self ) :
		# type: () -> int
		pass
	def getOurAttitudeModifier( self ) :
		# type: () -> int
		pass
	def getPlotExtraYield( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPopulationChange( self ) :
		# type: () -> int
		pass
	def getPrereqTech( self ) :
		# type: () -> int
		pass
	def getRandomGold( self ) :
		# type: () -> int
		pass
	def getRevoltTurns( self ) :
		# type: () -> int
		pass
	def getRoute( self ) :
		# type: () -> int
		pass
	def getRouteChange( self ) :
		# type: () -> int
		pass
	def getSpaceProductionModifier( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTech( self ) :
		# type: () -> int
		pass
	def getTechCostPercent( self ) :
		# type: () -> int
		pass
	def getTechFlavorValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def getTechMinTurnsLeft( self ) :
		# type: () -> int
		pass
	def getTechPercent( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTheirEnemyAttitudeModifier( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnitClass( self ) :
		# type: () -> int
		pass
	def getUnitClassPromotion( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitCombatPromotion( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitExperience( self ) :
		# type: () -> int
		pass
	def getUnitImmobileTurns( self ) :
		# type: () -> int
		pass
	def getUnitPromotion( self ) :
		# type: () -> int
		pass
	def isCityEffect( self ) :
		# type: () -> bool
		pass
	def isDeclareWar( self ) :
		# type: () -> bool
		pass
	def isDisbandUnit( self ) :
		# type: () -> bool
		pass
	def isGlobal( self ) :
		# type: () -> bool
		pass
	def isGoldToPlayer( self ) :
		# type: () -> bool
		pass
	def isGoldenAge( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isOtherPlayerCityEffect( self ) :
		# type: () -> bool
		pass
	def isQuest( self ) :
		# type: () -> bool
		pass
	def isTeam( self ) :
		# type: () -> bool
		pass

class CvEventTriggerInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAngry( self ) :
		# type: () -> int
		pass
	def getBonusRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCityFoodWeight( self ) :
		# type: () -> int
		pass
	def getCivic( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCorporationRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getEvent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFeatureRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getImprovementRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def getMaxOurLandmass( self ) :
		# type: () -> int
		pass
	def getMaxPopulation( self ) :
		# type: () -> int
		pass
	def getMinDifficulty( self ) :
		# type: () -> int
		pass
	def getMinMapLandmass( self ) :
		# type: () -> int
		pass
	def getMinOurLandmass( self ) :
		# type: () -> int
		pass
	def getMinPopulation( self ) :
		# type: () -> int
		pass
	def getMinTreasury( self ) :
		# type: () -> int
		pass
	def getNumBonusesRequired( self ) :
		# type: () -> int
		pass
	def getNumBuildings( self ) :
		# type: () -> int
		pass
	def getNumBuildingsGlobal( self ) :
		# type: () -> int
		pass
	def getNumBuildingsRequired( self ) :
		# type: () -> int
		pass
	def getNumCorporations( self ) :
		# type: () -> int
		pass
	def getNumCorporationsRequired( self ) :
		# type: () -> int
		pass
	def getNumEvents( self ) :
		# type: () -> int
		pass
	def getNumFeaturesRequired( self ) :
		# type: () -> int
		pass
	def getNumImprovementsRequired( self ) :
		# type: () -> int
		pass
	def getNumObsoleteTechs( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNumPlotsRequired( self ) :
		# type: () -> int
		pass
	def getNumPrereqAndTechs( self ) :
		# type: () -> int
		pass
	def getNumPrereqEvents( self ) :
		# type: () -> int
		pass
	def getNumPrereqOrTechs( self ) :
		# type: () -> int
		pass
	def getNumReligions( self ) :
		# type: () -> int
		pass
	def getNumReligionsRequired( self ) :
		# type: () -> int
		pass
	def getNumRoutesRequired( self ) :
		# type: () -> int
		pass
	def getNumTerrainsRequired( self ) :
		# type: () -> int
		pass
	def getNumUnits( self ) :
		# type: () -> int
		pass
	def getNumUnitsGlobal( self ) :
		# type: () -> int
		pass
	def getNumUnitsRequired( self ) :
		# type: () -> int
		pass
	def getObsoleteTech( self, arg0 ) :
		# type: (int) -> int
		pass
	def getOtherPlayerHasTech( self ) :
		# type: () -> int
		pass
	def getOtherPlayerShareBorders( self ) :
		# type: () -> int
		pass
	def getPercentGamesActive( self ) :
		# type: () -> int
		pass
	def getPlotsType( self ) :
		# type: () -> int
		pass
	def getPrereqAndTechs( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPrereqEvent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPrereqOrTechs( self, arg0 ) :
		# type: (int) -> int
		pass
	def getProbability( self ) :
		# type: () -> int
		pass
	def getReligionRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def getRouteRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTerrainRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnhealthy( self ) :
		# type: () -> int
		pass
	def getUnitDamagedWeight( self ) :
		# type: () -> int
		pass
	def getUnitDistanceWeight( self ) :
		# type: () -> int
		pass
	def getUnitExperienceWeight( self ) :
		# type: () -> int
		pass
	def getUnitRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def isGlobal( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isOtherPlayerAI( self ) :
		# type: () -> bool
		pass
	def isOtherPlayerHasOtherReligion( self ) :
		# type: () -> bool
		pass
	def isOtherPlayerHasReligion( self ) :
		# type: () -> bool
		pass
	def isOwnPlot( self ) :
		# type: () -> bool
		pass
	def isPickCity( self ) :
		# type: () -> bool
		pass
	def isPickOtherPlayerCity( self ) :
		# type: () -> bool
		pass
	def isPickPlayer( self ) :
		# type: () -> bool
		pass
	def isPickReligion( self ) :
		# type: () -> bool
		pass
	def isPrereqEventCity( self ) :
		# type: () -> bool
		pass
	def isProbabilityBuildingMultiply( self ) :
		# type: () -> bool
		pass
	def isProbabilityUnitMultiply( self ) :
		# type: () -> bool
		pass
	def isRecurring( self ) :
		# type: () -> bool
		pass
	def isSinglePlayer( self ) :
		# type: () -> bool
		pass
	def isStateReligion( self ) :
		# type: () -> bool
		pass
	def isTeam( self ) :
		# type: () -> bool
		pass
	def isUnitsOnPlot( self ) :
		# type: () -> bool
		pass

class CvFeatureInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAdvancedStartRemoveCost( self ) :
		# type: () -> int
		pass
	def getAppearanceProbability( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefenseModifier( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDisappearanceProbability( self ) :
		# type: () -> int
		pass
	def getGrowthProbability( self ) :
		# type: () -> int
		pass
	def getHealthPercent( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHillsYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getMovementCost( self ) :
		# type: () -> int
		pass
	def getNumVarieties( self ) :
		# type: () -> int
		pass
	def getRiverYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSeeThroughChange( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTurnDamage( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def isAddsFreshWater( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isImpassable( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isNoAdjacent( self ) :
		# type: () -> bool
		pass
	def isNoCity( self ) :
		# type: () -> bool
		pass
	def isNoCoast( self ) :
		# type: () -> bool
		pass
	def isNoImprovement( self ) :
		# type: () -> bool
		pass
	def isNoRiver( self ) :
		# type: () -> bool
		pass
	def isNukeImmune( self ) :
		# type: () -> bool
		pass
	def isRequiresFlatlands( self ) :
		# type: () -> bool
		pass
	def isRequiresRiver( self ) :
		# type: () -> bool
		pass
	def isTerrain( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isVisibleAlways( self ) :
		# type: () -> bool
		pass

class CvForceControlInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefault( self ) :
		# type: () -> bool
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvGameOptionInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefault( self ) :
		# type: () -> bool
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getVisible( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvGameSpeedInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAnarchyPercent( self ) :
		# type: () -> int
		pass
	def getBarbPercent( self ) :
		# type: () -> int
		pass
	def getBuildPercent( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getConstructPercent( self ) :
		# type: () -> int
		pass
	def getCreatePercent( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getFeatureProductionPercent( self ) :
		# type: () -> int
		pass
	def getGameTurnInfo( self ) :
		# type: () -> GameTurnInfo
		pass
	def getGoldenAgePercent( self ) :
		# type: () -> int
		pass
	def getGreatPeoplePercent( self ) :
		# type: () -> int
		pass
	def getGrowthPercent( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHurryConscriptAngerPercent( self ) :
		# type: () -> int
		pass
	def getHurryPercent( self ) :
		# type: () -> int
		pass
	def getImprovementPercent( self ) :
		# type: () -> int
		pass
	def getInflationOffset( self ) :
		# type: () -> int
		pass
	def getInflationPercent( self ) :
		# type: () -> int
		pass
	def getNumTurnIncrements( self ) :
		# type: () -> int
		pass
	def getResearchPercent( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTrainPercent( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnitDiscoverPercent( self ) :
		# type: () -> int
		pass
	def getUnitGreatWorkPercent( self ) :
		# type: () -> int
		pass
	def getUnitHurryPercent( self ) :
		# type: () -> int
		pass
	def getUnitTradePercent( self ) :
		# type: () -> int
		pass
	def getVictoryDelayPercent( self ) :
		# type: () -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvGameText( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getNumLanguages( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def setText( self, arg0 ) :
		# type: (unicode) -> None
		pass

class CvGoodyInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getBarbarianUnitClass( self ) :
		# type: () -> int
		pass
	def getBarbarianUnitProb( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDamagePrereq( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getExperience( self ) :
		# type: () -> int
		pass
	def getGold( self ) :
		# type: () -> int
		pass
	def getGoldRand1( self ) :
		# type: () -> int
		pass
	def getGoldRand2( self ) :
		# type: () -> int
		pass
	def getHealing( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getMapOffset( self ) :
		# type: () -> int
		pass
	def getMapProb( self ) :
		# type: () -> int
		pass
	def getMapRange( self ) :
		# type: () -> int
		pass
	def getMinBarbarians( self ) :
		# type: () -> int
		pass
	def getSound( self ) :
		# type: () -> str
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnitClassType( self ) :
		# type: () -> int
		pass
	def isBad( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isTech( self ) :
		# type: () -> bool
		pass

class CvGraphicOptionInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefault( self ) :
		# type: () -> bool
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvHandicapInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAIAdvancedStartPercent( self ) :
		# type: () -> int
		pass
	def getAIAnimalCombatModifier( self ) :
		# type: () -> int
		pass
	def getAIBarbarianCombatModifier( self ) :
		# type: () -> int
		pass
	def getAICivicUpkeepPercent( self ) :
		# type: () -> int
		pass
	def getAIConstructPercent( self ) :
		# type: () -> int
		pass
	def getAICreatePercent( self ) :
		# type: () -> int
		pass
	def getAIDeclareWarProb( self ) :
		# type: () -> int
		pass
	def getAIGrowthPercent( self ) :
		# type: () -> int
		pass
	def getAIInflationPercent( self ) :
		# type: () -> int
		pass
	def getAIPerEraModifier( self ) :
		# type: () -> int
		pass
	def getAIStartingDefenseUnits( self ) :
		# type: () -> int
		pass
	def getAIStartingExploreUnits( self ) :
		# type: () -> int
		pass
	def getAIStartingUnitMultiplier( self ) :
		# type: () -> int
		pass
	def getAIStartingWorkerUnits( self ) :
		# type: () -> int
		pass
	def getAITrainPercent( self ) :
		# type: () -> int
		pass
	def getAIUnitCostPercent( self ) :
		# type: () -> int
		pass
	def getAIUnitSupplyPercent( self ) :
		# type: () -> int
		pass
	def getAIUnitUpgradePercent( self ) :
		# type: () -> int
		pass
	def getAIWarWearinessPercent( self ) :
		# type: () -> int
		pass
	def getAIWorkRateModifier( self ) :
		# type: () -> int
		pass
	def getAIWorldConstructPercent( self ) :
		# type: () -> int
		pass
	def getAIWorldCreatePercent( self ) :
		# type: () -> int
		pass
	def getAIWorldTrainPercent( self ) :
		# type: () -> int
		pass
	def getAnimalAttackProb( self ) :
		# type: () -> int
		pass
	def getAnimalCombatModifier( self ) :
		# type: () -> int
		pass
	def getAttitudeChange( self ) :
		# type: () -> int
		pass
	def getBarbarianCityCreationProb( self ) :
		# type: () -> int
		pass
	def getBarbarianCityCreationTurnsElapsed( self ) :
		# type: () -> int
		pass
	def getBarbarianCombatModifier( self ) :
		# type: () -> int
		pass
	def getBarbarianCreationTurnsElapsed( self ) :
		# type: () -> int
		pass
	def getBarbarianInitialDefenders( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivicUpkeepPercent( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getColonyMaintenancePercent( self ) :
		# type: () -> int
		pass
	def getCorporationMaintenancePercent( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDistanceMaintenancePercent( self ) :
		# type: () -> int
		pass
	def getFreeUnits( self ) :
		# type: () -> int
		pass
	def getFreeWinsVsBarbs( self ) :
		# type: () -> int
		pass
	def getGoodies( self, arg0 ) :
		# type: (int) -> int
		pass
	def getHappyBonus( self ) :
		# type: () -> int
		pass
	def getHealthBonus( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getInflationPercent( self ) :
		# type: () -> int
		pass
	def getMaxColonyMaintenance( self ) :
		# type: () -> int
		pass
	def getMaxNumCitiesMaintenance( self ) :
		# type: () -> int
		pass
	def getNoTechTradeModifier( self ) :
		# type: () -> int
		pass
	def getNumCitiesMaintenancePercent( self ) :
		# type: () -> int
		pass
	def getNumGoodies( self ) :
		# type: () -> int
		pass
	def getResearchPercent( self ) :
		# type: () -> int
		pass
	def getStartingDefenseUnits( self ) :
		# type: () -> int
		pass
	def getStartingExploreUnits( self ) :
		# type: () -> int
		pass
	def getStartingGold( self ) :
		# type: () -> int
		pass
	def getStartingLocationPercent( self ) :
		# type: () -> int
		pass
	def getStartingWorkerUnits( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechTradeKnownModifier( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnitCostPercent( self ) :
		# type: () -> int
		pass
	def getUnownedTilesPerBarbarianCity( self ) :
		# type: () -> int
		pass
	def getUnownedTilesPerBarbarianUnit( self ) :
		# type: () -> int
		pass
	def getUnownedTilesPerGameAnimal( self ) :
		# type: () -> int
		pass
	def getUnownedWaterTilesPerBarbarianUnit( self ) :
		# type: () -> int
		pass
	def isAIFreeTechs( self, arg0 ) :
		# type: (int) -> int
		pass
	def isFreeTechs( self, arg0 ) :
		# type: (int) -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvHurryInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getGoldPerProduction( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getProductionPerPopulation( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isAnger( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvImprovementBonusInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDiscoverRand( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def isBonusMakesValid( self ) :
		# type: () -> bool
		pass
	def isBonusTrade( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvImprovementInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAirBombDefense( self ) :
		# type: () -> int
		pass
	def getArtDefineTag( self ) :
		# type: () -> str
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefenseModifier( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getFeatureGrowthProbability( self ) :
		# type: () -> int
		pass
	def getFeatureMakesValid( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getGoodyUniqueRange( self ) :
		# type: () -> int
		pass
	def getHappiness( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHillsYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getImprovementBonusDiscoverRand( self, arg0 ) :
		# type: (int) -> int
		pass
	def getImprovementBonusYield( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getImprovementPillage( self ) :
		# type: () -> int
		pass
	def getImprovementUpgrade( self ) :
		# type: () -> int
		pass
	def getIrrigatedYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPillageGold( self ) :
		# type: () -> int
		pass
	def getPrereqNatureYield( self, arg0 ) :
		# type: (int) -> int
		pass
	def getRiverSideYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getRouteYieldChanges( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechYieldChanges( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getTerrainMakesValid( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTilesPerGoody( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUpgradeTime( self ) :
		# type: () -> int
		pass
	def getYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def isActsAsCity( self ) :
		# type: () -> bool
		pass
	def isCarriesIrrigation( self ) :
		# type: () -> bool
		pass
	def isFreshWaterMakesValid( self ) :
		# type: () -> bool
		pass
	def isGoody( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isHillsMakesValid( self ) :
		# type: () -> bool
		pass
	def isImprovementBonusMakesValid( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isImprovementBonusTrade( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isNoFreshWater( self ) :
		# type: () -> bool
		pass
	def isOutsideBorders( self ) :
		# type: () -> bool
		pass
	def isPermanent( self ) :
		# type: () -> bool
		pass
	def isRequiresFeature( self ) :
		# type: () -> bool
		pass
	def isRequiresFlatlands( self ) :
		# type: () -> bool
		pass
	def isRequiresIrrigation( self ) :
		# type: () -> bool
		pass
	def isRequiresRiverSide( self ) :
		# type: () -> bool
		pass
	def isRiverSideMakesValid( self ) :
		# type: () -> bool
		pass
	def isWater( self ) :
		# type: () -> bool
		pass

class CvInfoBase( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvInterfaceModeInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCursorIndex( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getGotoPlot( self ) :
		# type: () -> bool
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHighlightPlot( self ) :
		# type: () -> bool
		pass
	def getMissionType( self ) :
		# type: () -> int
		pass
	def getSelectAll( self ) :
		# type: () -> bool
		pass
	def getSelectType( self ) :
		# type: () -> bool
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getVisible( self ) :
		# type: () -> bool
		pass
	def isAltDown( self ) :
		# type: () -> bool
		pass
	def isAltDownAlt( self ) :
		# type: () -> bool
		pass
	def isCtrlDown( self ) :
		# type: () -> bool
		pass
	def isCtrlDownAlt( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isShiftDown( self ) :
		# type: () -> bool
		pass
	def isShiftDownAlt( self ) :
		# type: () -> bool
		pass

class CvLeaderHeadInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAdoptCivicRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getArtDefineTag( self ) :
		# type: () -> str
		pass
	def getAtPeaceAttitudeChangeLimit( self ) :
		# type: () -> int
		pass
	def getAtPeaceAttitudeDivisor( self ) :
		# type: () -> int
		pass
	def getAtWarAttitudeChangeLimit( self ) :
		# type: () -> int
		pass
	def getAtWarAttitudeDivisor( self ) :
		# type: () -> int
		pass
	def getAttackOddsChangeRand( self ) :
		# type: () -> int
		pass
	def getBaseAttackOddsChange( self ) :
		# type: () -> int
		pass
	def getBaseAttitude( self ) :
		# type: () -> int
		pass
	def getBasePeaceWeight( self ) :
		# type: () -> int
		pass
	def getBetterRankDifferenceAttitudeChange( self ) :
		# type: () -> int
		pass
	def getBonusTradeAttitudeChangeLimit( self ) :
		# type: () -> int
		pass
	def getBonusTradeAttitudeDivisor( self ) :
		# type: () -> int
		pass
	def getBuildUnitProb( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCloseBordersAttitudeChange( self ) :
		# type: () -> int
		pass
	def getContactDelay( self, arg0 ) :
		# type: (int) -> int
		pass
	def getContactRand( self, arg0 ) :
		# type: (int) -> int
		pass
	def getConvertReligionRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getDeclareWarRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getDeclareWarThemRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getDeclareWarTradeRand( self ) :
		# type: () -> int
		pass
	def getDefensivePactAttitudeChangeLimit( self ) :
		# type: () -> int
		pass
	def getDefensivePactAttitudeDivisor( self ) :
		# type: () -> int
		pass
	def getDefensivePactRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getDemandRebukedSneakProb( self ) :
		# type: () -> int
		pass
	def getDemandRebukedWarProb( self ) :
		# type: () -> int
		pass
	def getDemandTributeAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDifferentReligionAttitudeChange( self ) :
		# type: () -> int
		pass
	def getDifferentReligionAttitudeChangeLimit( self ) :
		# type: () -> int
		pass
	def getDifferentReligionAttitudeDivisor( self ) :
		# type: () -> int
		pass
	def getDiploPeaceIntroMusicScriptIds( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDiploPeaceMusicScriptIds( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDiploWarIntroMusicScriptIds( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDiploWarMusicScriptIds( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDogpileWarRand( self ) :
		# type: () -> int
		pass
	def getEspionageWeight( self ) :
		# type: () -> int
		pass
	def getFavoriteCivic( self ) :
		# type: () -> int
		pass
	def getFavoriteCivicAttitudeChange( self ) :
		# type: () -> int
		pass
	def getFavoriteCivicAttitudeChangeLimit( self ) :
		# type: () -> int
		pass
	def getFavoriteCivicAttitudeDivisor( self ) :
		# type: () -> int
		pass
	def getFavoriteReligion( self ) :
		# type: () -> int
		pass
	def getFlavorValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFreedomAppreciation( self ) :
		# type: () -> int
		pass
	def getHappinessBonusRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getHealthBonusRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getImprovementWeightModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getLeaderHead( self ) :
		# type: () -> str
		pass
	def getLimitedWarPowerRatio( self ) :
		# type: () -> int
		pass
	def getLimitedWarRand( self ) :
		# type: () -> int
		pass
	def getLostWarAttitudeChange( self ) :
		# type: () -> int
		pass
	def getMakePeaceRand( self ) :
		# type: () -> int
		pass
	def getMapRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getMaxGoldPerTurnTradePercent( self ) :
		# type: () -> int
		pass
	def getMaxGoldTradePercent( self ) :
		# type: () -> int
		pass
	def getMaxWarDistantPowerRatio( self ) :
		# type: () -> int
		pass
	def getMaxWarMinAdjacentLandPercent( self ) :
		# type: () -> int
		pass
	def getMaxWarNearbyPowerRatio( self ) :
		# type: () -> int
		pass
	def getMaxWarRand( self ) :
		# type: () -> int
		pass
	def getMemoryAttitudePercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getMemoryDecayRand( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNoGiveHelpAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getNoTechTradeThreshold( self ) :
		# type: () -> int
		pass
	def getNoWarAttitudeProb( self, arg0 ) :
		# type: (int) -> int
		pass
	def getOpenBordersAttitudeChangeLimit( self ) :
		# type: () -> int
		pass
	def getOpenBordersAttitudeDivisor( self ) :
		# type: () -> int
		pass
	def getOpenBordersRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getPeaceWeightRand( self ) :
		# type: () -> int
		pass
	def getPermanentAllianceRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getRazeCityProb( self ) :
		# type: () -> int
		pass
	def getRefuseToTalkWarThreshold( self ) :
		# type: () -> int
		pass
	def getSameReligionAttitudeChange( self ) :
		# type: () -> int
		pass
	def getSameReligionAttitudeChangeLimit( self ) :
		# type: () -> int
		pass
	def getSameReligionAttitudeDivisor( self ) :
		# type: () -> int
		pass
	def getShareWarAttitudeChange( self ) :
		# type: () -> int
		pass
	def getShareWarAttitudeChangeLimit( self ) :
		# type: () -> int
		pass
	def getShareWarAttitudeDivisor( self ) :
		# type: () -> int
		pass
	def getStopTradingRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getStopTradingThemRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getStrategicBonusRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getTechTradeKnownPercent( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnitAIWeightModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getVassalPowerModifier( self ) :
		# type: () -> int
		pass
	def getVassalRefuseAttitudeThreshold( self ) :
		# type: () -> int
		pass
	def getWarmongerRespect( self ) :
		# type: () -> int
		pass
	def getWonderConstructRand( self ) :
		# type: () -> int
		pass
	def getWorseRankDifferenceAttitudeChange( self ) :
		# type: () -> int
		pass
	def hasTrait( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvMPOptionInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefault( self ) :
		# type: () -> bool
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvMainMenuInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getLoading( self ) :
		# type: () -> str
		pass
	def getLoadingSlideshow( self ) :
		# type: () -> str
		pass
	def getScene( self ) :
		# type: () -> str
		pass
	def getSceneNoShader( self ) :
		# type: () -> str
		pass
	def getSoundtrack( self ) :
		# type: () -> str
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvMissionInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTime( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getVisible( self ) :
		# type: () -> bool
		pass
	def getWaypoint( self ) :
		# type: () -> str
		pass
	def isBuild( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isSound( self ) :
		# type: () -> bool
		pass
	def isTarget( self ) :
		# type: () -> bool
		pass

class CvPlayerColorInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getColorTypePrimary( self ) :
		# type: () -> int
		pass
	def getColorTypeSecondary( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextColorType( self ) :
		# type: () -> int
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvPlayerOptionInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefault( self ) :
		# type: () -> bool
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvProcessInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getProductionToCommerceModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechPrereq( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvProjectInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAnyoneProjectPrereq( self ) :
		# type: () -> int
		pass
	def getBonusProductionModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCreateSound( self ) :
		# type: () -> str
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getEveryoneSpecialBuilding( self ) :
		# type: () -> int
		pass
	def getEveryoneSpecialUnit( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getMaxGlobalInstances( self ) :
		# type: () -> int
		pass
	def getMaxTeamInstances( self ) :
		# type: () -> int
		pass
	def getMovieArtDef( self ) :
		# type: () -> str
		pass
	def getNukeInterception( self ) :
		# type: () -> int
		pass
	def getProductionCost( self ) :
		# type: () -> int
		pass
	def getProjectsNeeded( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getSuccessRate( self ) :
		# type: () -> int
		pass
	def getTechPrereq( self ) :
		# type: () -> int
		pass
	def getTechShare( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getVictoryDelayPercent( self ) :
		# type: () -> int
		pass
	def getVictoryMinThreshold( self, arg0 ) :
		# type: (int) -> int
		pass
	def getVictoryPrereq( self ) :
		# type: () -> int
		pass
	def getVictoryThreshold( self, arg0 ) :
		# type: (int) -> int
		pass
	def isAllowsNukes( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isSpaceship( self ) :
		# type: () -> bool
		pass

class CvPromotionInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getActionInfoIndex( self ) :
		# type: () -> int
		pass
	def getAdjacentTileHealChange( self ) :
		# type: () -> int
		pass
	def getAirRangeChange( self ) :
		# type: () -> int
		pass
	def getBombardRateChange( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCargoChange( self ) :
		# type: () -> int
		pass
	def getChanceFirstStrikesChange( self ) :
		# type: () -> int
		pass
	def getCityAttackPercent( self ) :
		# type: () -> int
		pass
	def getCityDefensePercent( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCollateralDamageChange( self ) :
		# type: () -> int
		pass
	def getCollateralDamageProtection( self ) :
		# type: () -> int
		pass
	def getCombatPercent( self ) :
		# type: () -> int
		pass
	def getCommandType( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDomainModifierPercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getEnemyHealChange( self ) :
		# type: () -> int
		pass
	def getEvasionChange( self ) :
		# type: () -> int
		pass
	def getExperiencePercent( self ) :
		# type: () -> int
		pass
	def getFeatureAttackPercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFeatureDefensePercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFeatureDoubleMove( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getFirstStrikesChange( self ) :
		# type: () -> int
		pass
	def getFriendlyHealChange( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHillsAttackPercent( self ) :
		# type: () -> int
		pass
	def getHillsDefensePercent( self ) :
		# type: () -> int
		pass
	def getInterceptChange( self ) :
		# type: () -> int
		pass
	def getKamikazePercent( self ) :
		# type: () -> int
		pass
	def getMoveDiscountChange( self ) :
		# type: () -> int
		pass
	def getMovesChange( self ) :
		# type: () -> int
		pass
	def getNeutralHealChange( self ) :
		# type: () -> int
		pass
	def getPillageChange( self ) :
		# type: () -> int
		pass
	def getPrereqOrPromotion1( self ) :
		# type: () -> int
		pass
	def getPrereqOrPromotion2( self ) :
		# type: () -> int
		pass
	def getPrereqPromotion( self ) :
		# type: () -> int
		pass
	def getRevoltProtection( self ) :
		# type: () -> int
		pass
	def getSameTileHealChange( self ) :
		# type: () -> int
		pass
	def getSound( self ) :
		# type: () -> str
		pass
	def getStateReligionPrereq( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechPrereq( self ) :
		# type: () -> int
		pass
	def getTerrainAttackPercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getTerrainDefensePercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getTerrainDoubleMove( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnitCombat( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getUnitCombatModifierPercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUpgradeDiscount( self ) :
		# type: () -> int
		pass
	def getVisibilityChange( self ) :
		# type: () -> int
		pass
	def getWithdrawalChange( self ) :
		# type: () -> int
		pass
	def isAlwaysHeal( self ) :
		# type: () -> bool
		pass
	def isAmphib( self ) :
		# type: () -> bool
		pass
	def isBlitz( self ) :
		# type: () -> bool
		pass
	def isEnemyRoute( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isHillsDoubleMove( self ) :
		# type: () -> bool
		pass
	def isImmuneToFirstStrikes( self ) :
		# type: () -> bool
		pass
	def isLeader( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isRiver( self ) :
		# type: () -> bool
		pass

class CvQuestInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getNumQuestLinks( self ) :
		# type: () -> int
		pass
	def getNumQuestMessages( self ) :
		# type: () -> str
		pass
	def getNumQuestSounds( self ) :
		# type: () -> int
		pass
	def getQuestBodyText( self ) :
		# type: () -> str
		pass
	def getQuestLinkName( self ) :
		# type: () -> str
		pass
	def getQuestLinkType( self ) :
		# type: () -> str
		pass
	def getQuestMessages( self ) :
		# type: () -> int
		pass
	def getQuestObjective( self ) :
		# type: () -> str
		pass
	def getQuestSounds( self ) :
		# type: () -> str
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def setNumQuestMessages( self, arg0 ) :
		# type: (int) -> None
		pass
	def setQuestBodyText( self, arg0 ) :
		# type: (str) -> None
		pass
	def setQuestMessages( self, arg0, arg1 ) :
		# type: (int, str) -> None
		pass
	def setQuestObjective( self, arg0 ) :
		# type: (str) -> None
		pass

class CvReligionInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAdjectiveKey( self ) :
		# type: () -> unicode
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getButtonDisabled( self ) :
		# type: () -> str
		pass
	def getChar( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getFreeUnitClass( self ) :
		# type: () -> int
		pass
	def getGenericTechButton( self ) :
		# type: () -> str
		pass
	def getGlobalReligionCommerce( self, arg0 ) :
		# type: (int) -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHolyCityChar( self ) :
		# type: () -> int
		pass
	def getHolyCityCommerce( self, arg0 ) :
		# type: (int) -> int
		pass
	def getMissionType( self ) :
		# type: () -> int
		pass
	def getMovieFile( self ) :
		# type: () -> str
		pass
	def getMovieSound( self ) :
		# type: () -> str
		pass
	def getNumFreeUnits( self ) :
		# type: () -> int
		pass
	def getSound( self ) :
		# type: () -> str
		pass
	def getSpreadFactor( self ) :
		# type: () -> int
		pass
	def getStateReligionCommerce( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechButton( self ) :
		# type: () -> str
		pass
	def getTechPrereq( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvRouteInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getFlatMovementCost( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getMovementCost( self ) :
		# type: () -> int
		pass
	def getPrereqBonus( self ) :
		# type: () -> int
		pass
	def getPrereqOrBonus( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechMovementChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getValue( self ) :
		# type: () -> int
		pass
	def getYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvRouteModelInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getConnectString( self ) :
		# type: () -> str
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getModelConnectString( self ) :
		# type: () -> str
		pass
	def getModelFile( self ) :
		# type: () -> str
		pass
	def getModelFileKey( self ) :
		# type: () -> str
		pass
	def getRotateString( self ) :
		# type: () -> str
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def setModelFile( self, arg0 ) :
		# type: (str) -> None
		pass
	def setModelFileKey( self, arg0 ) :
		# type: (str) -> None
		pass

class CvScalableInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass

class CvSeaLevelInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getSeaLevelChange( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvSpecialBuildingInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getObsoleteTech( self ) :
		# type: () -> int
		pass
	def getProductionTraits( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTechPrereq( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isValid( self ) :
		# type: () -> bool
		pass

class CvSpecialUnitInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getProductionTraits( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isCarrierUnitAIType( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isCityLoad( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isValid( self ) :
		# type: () -> bool
		pass

class CvSpecialistInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCommerceChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getExperience( self ) :
		# type: () -> int
		pass
	def getFlavorValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def getGreatPeopleRateChange( self ) :
		# type: () -> int
		pass
	def getGreatPeopleUnitClass( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getMissionType( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTexture( self ) :
		# type: () -> str
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isVisible( self ) :
		# type: () -> bool
		pass

class CvTechInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAITradeModifier( self ) :
		# type: () -> int
		pass
	def getAIWeight( self ) :
		# type: () -> int
		pass
	def getAdvisorType( self ) :
		# type: () -> int
		pass
	def getAssetValue( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDomainExtraMoves( self, arg0 ) :
		# type: (int) -> int
		pass
	def getEra( self ) :
		# type: () -> int
		pass
	def getFeatureProductionModifier( self ) :
		# type: () -> int
		pass
	def getFirstFreeTechs( self ) :
		# type: () -> int
		pass
	def getFirstFreeUnitClass( self ) :
		# type: () -> int
		pass
	def getFlavorValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def getGridX( self ) :
		# type: () -> int
		pass
	def getGridY( self ) :
		# type: () -> int
		pass
	def getHappiness( self ) :
		# type: () -> int
		pass
	def getHealth( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getPowerValue( self ) :
		# type: () -> int
		pass
	def getPrereqAndTechs( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPrereqOrTechs( self, arg0 ) :
		# type: (int) -> int
		pass
	def getQuote( self ) :
		# type: () -> unicode
		pass
	def getResearchCost( self ) :
		# type: () -> int
		pass
	def getSound( self ) :
		# type: () -> str
		pass
	def getSoundMP( self ) :
		# type: () -> str
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTradeRoutes( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getWorkerSpeedModifier( self ) :
		# type: () -> int
		pass
	def isBridgeBuilding( self ) :
		# type: () -> bool
		pass
	def isCommerceFlexible( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isDefensivePactTrading( self ) :
		# type: () -> bool
		pass
	def isDisable( self ) :
		# type: () -> bool
		pass
	def isExtraWaterSeeFrom( self ) :
		# type: () -> bool
		pass
	def isGoldTrading( self ) :
		# type: () -> bool
		pass
	def isGoodyTech( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isIgnoreIrrigation( self ) :
		# type: () -> bool
		pass
	def isIrrigation( self ) :
		# type: () -> bool
		pass
	def isMapCentering( self ) :
		# type: () -> bool
		pass
	def isMapTrading( self ) :
		# type: () -> bool
		pass
	def isMapVisible( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isOpenBordersTrading( self ) :
		# type: () -> bool
		pass
	def isPermanentAllianceTrading( self ) :
		# type: () -> bool
		pass
	def isRepeat( self ) :
		# type: () -> bool
		pass
	def isRiverTrade( self ) :
		# type: () -> bool
		pass
	def isTechTrading( self ) :
		# type: () -> bool
		pass
	def isTerrainTrade( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isTrade( self ) :
		# type: () -> bool
		pass
	def isVassalStateTrading( self ) :
		# type: () -> bool
		pass
	def isWaterWork( self ) :
		# type: () -> bool
		pass

class CvTerrainInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getBuildModifier( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefenseModifier( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHillsYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getMovementCost( self ) :
		# type: () -> int
		pass
	def getRiverYieldChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSeeFromLevel( self ) :
		# type: () -> int
		pass
	def getSeeThroughLevel( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getYield( self, arg0 ) :
		# type: (int) -> int
		pass
	def isFound( self ) :
		# type: () -> bool
		pass
	def isFoundCoast( self ) :
		# type: () -> bool
		pass
	def isFoundFreshWater( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isImpassable( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isWater( self ) :
		# type: () -> bool
		pass

class CvTraitInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCommerceChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCommerceModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDomesticGreatGeneralRateModifier( self ) :
		# type: () -> int
		pass
	def getExtraYieldThreshold( self, arg0 ) :
		# type: (int) -> int
		pass
	def getGreatGeneralRateModifier( self ) :
		# type: () -> int
		pass
	def getGreatPeopleRateModifier( self ) :
		# type: () -> int
		pass
	def getHappiness( self ) :
		# type: () -> int
		pass
	def getHealth( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getLevelExperienceModifier( self ) :
		# type: () -> int
		pass
	def getMaxAnarchy( self ) :
		# type: () -> int
		pass
	def getMaxGlobalBuildingProductionModifier( self ) :
		# type: () -> int
		pass
	def getMaxPlayerBuildingProductionModifier( self ) :
		# type: () -> int
		pass
	def getMaxTeamBuildingProductionModifier( self ) :
		# type: () -> int
		pass
	def getShortDescription( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTradeYieldModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUpkeepModifier( self ) :
		# type: () -> int
		pass
	def isFreePromotion( self, arg0 ) :
		# type: (int) -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvTurnTimerInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getBaseTime( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCityBonus( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getFirstTurnMultiplier( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnitBonus( self ) :
		# type: () -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvTutorialInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getNextTutorialInfoType( self ) :
		# type: () -> str
		pass
	def getNumTutorialMessages( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTutorialMessage( self, arg0 ) :
		# type: (int) -> CvTutorialMessage
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvTutorialMessage( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getImage( self ) :
		# type: () -> str
		pass
	def getNumTutorialScripts( self ) :
		# type: () -> int
		pass
	def getSound( self ) :
		# type: () -> str
		pass
	def getText( self ) :
		# type: () -> str
		pass
	def getTutorialScriptByIndex( self, arg0 ) :
		# type: (int) -> int
		pass

class CvUnitClassInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDefaultUnitIndex( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getInstanceCostModifier( self ) :
		# type: () -> int
		pass
	def getMaxGlobalInstances( self ) :
		# type: () -> int
		pass
	def getMaxPlayerInstances( self ) :
		# type: () -> int
		pass
	def getMaxTeamInstances( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvUnitInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAIWeight( self ) :
		# type: () -> int
		pass
	def getAdvisorType( self ) :
		# type: () -> int
		pass
	def getAirCombat( self ) :
		# type: () -> int
		pass
	def getAirCombatLimit( self ) :
		# type: () -> int
		pass
	def getAirRange( self ) :
		# type: () -> int
		pass
	def getAirUnitCap( self ) :
		# type: () -> int
		pass
	def getAnimalCombatModifier( self ) :
		# type: () -> int
		pass
	def getArtInfo( self, arg0, arg1 ) :
		# type: (int, bool) -> CvArtInfoUnit
		pass
	def getAssetValue( self ) :
		# type: () -> int
		pass
	def getBaseDiscover( self ) :
		# type: () -> int
		pass
	def getBaseHurry( self ) :
		# type: () -> int
		pass
	def getBaseTrade( self ) :
		# type: () -> int
		pass
	def getBombRate( self ) :
		# type: () -> int
		pass
	def getBombardRate( self ) :
		# type: () -> int
		pass
	def getBonusProductionModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildings( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getBuilds( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCargoSpace( self ) :
		# type: () -> int
		pass
	def getChanceFirstStrikes( self ) :
		# type: () -> int
		pass
	def getCityAttackModifier( self ) :
		# type: () -> int
		pass
	def getCityDefenseModifier( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getCollateralDamage( self ) :
		# type: () -> int
		pass
	def getCollateralDamageLimit( self ) :
		# type: () -> int
		pass
	def getCollateralDamageMaxUnits( self ) :
		# type: () -> int
		pass
	def getCombat( self ) :
		# type: () -> int
		pass
	def getCombatLimit( self ) :
		# type: () -> int
		pass
	def getCommandType( self ) :
		# type: () -> int
		pass
	def getConscriptionValue( self ) :
		# type: () -> int
		pass
	def getCorporationSpreads( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCultureGarrisonValue( self ) :
		# type: () -> int
		pass
	def getDefaultUnitAIType( self ) :
		# type: () -> int
		pass
	def getDefenderUnitClass( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getDefenderUnitCombat( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDiscoverMultiplier( self ) :
		# type: () -> int
		pass
	def getDomainCargo( self ) :
		# type: () -> int
		pass
	def getDomainModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDomainType( self ) :
		# type: () -> int
		pass
	def getDropRange( self ) :
		# type: () -> int
		pass
	def getEarlyArtDefineTag( self, arg0, arg1 ) :
		# type: (int, UnitArtStyleTypes) -> str
		pass
	def getEspionagePoints( self ) :
		# type: () -> int
		pass
	def getEvasionProbability( self ) :
		# type: () -> int
		pass
	def getExtraCost( self ) :
		# type: () -> int
		pass
	def getFeatureAttackModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFeatureDefenseModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFeatureImpassable( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getFeatureNative( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getFeaturePassableTech( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFirstStrikes( self ) :
		# type: () -> int
		pass
	def getFlankingStrikeUnitClass( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFlavorValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def getForceBuildings( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getFreePromotions( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getGreatPeoples( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getGreatWorkCulture( self ) :
		# type: () -> int
		pass
	def getGroupDefinitions( self ) :
		# type: () -> int
		pass
	def getGroupSize( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHillsAttackModifier( self ) :
		# type: () -> int
		pass
	def getHillsDefenseModifier( self ) :
		# type: () -> int
		pass
	def getHolyCity( self ) :
		# type: () -> int
		pass
	def getHurryCostModifier( self ) :
		# type: () -> int
		pass
	def getHurryMultiplier( self ) :
		# type: () -> int
		pass
	def getInterceptionProbability( self ) :
		# type: () -> int
		pass
	def getInvisibleType( self ) :
		# type: () -> int
		pass
	def getLateArtDefineTag( self, arg0, arg1 ) :
		# type: (int, UnitArtStyleTypes) -> str
		pass
	def getLeaderExperience( self ) :
		# type: () -> int
		pass
	def getLeaderPromotion( self ) :
		# type: () -> int
		pass
	def getMeleeWaveSize( self ) :
		# type: () -> int
		pass
	def getMiddleArtDefineTag( self, arg0, arg1 ) :
		# type: (int, UnitArtStyleTypes) -> str
		pass
	def getMinAreaSize( self ) :
		# type: () -> int
		pass
	def getMoves( self ) :
		# type: () -> int
		pass
	def getNotUnitAIType( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getNukeRange( self ) :
		# type: () -> int
		pass
	def getNumSeeInvisibleTypes( self ) :
		# type: () -> int
		pass
	def getNumUnitNames( self ) :
		# type: () -> int
		pass
	def getPowerValue( self ) :
		# type: () -> int
		pass
	def getPrereqAndBonus( self ) :
		# type: () -> int
		pass
	def getPrereqAndTech( self ) :
		# type: () -> int
		pass
	def getPrereqAndTechs( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPrereqBuilding( self ) :
		# type: () -> int
		pass
	def getPrereqCorporation( self ) :
		# type: () -> int
		pass
	def getPrereqOrBonuses( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPrereqReligion( self ) :
		# type: () -> int
		pass
	def getProductionCost( self ) :
		# type: () -> int
		pass
	def getProductionTraits( self, arg0 ) :
		# type: (int) -> int
		pass
	def getRangedWaveSize( self ) :
		# type: () -> int
		pass
	def getReligionSpreads( self, arg0 ) :
		# type: (int) -> int
		pass
	def getReligionType( self ) :
		# type: () -> int
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def getSeeInvisibleType( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSpecialCargo( self ) :
		# type: () -> int
		pass
	def getSpecialUnitType( self ) :
		# type: () -> int
		pass
	def getStateReligion( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTargetUnitClass( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getTargetUnitCombat( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getTerrainAttackModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getTerrainDefenseModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getTerrainImpassable( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getTerrainNative( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getTerrainPassableTech( self, arg0 ) :
		# type: (int) -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTradeMultiplier( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnitAIType( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getUnitCaptureClassType( self ) :
		# type: () -> int
		pass
	def getUnitClassAttackModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitClassDefenseModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitClassType( self ) :
		# type: () -> int
		pass
	def getUnitCombatModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitCombatType( self ) :
		# type: () -> int
		pass
	def getUnitGroupRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitMaxSpeed( self ) :
		# type: () -> float
		pass
	def getUnitNames( self, arg0 ) :
		# type: (int) -> str
		pass
	def getUnitPadTime( self ) :
		# type: () -> float
		pass
	def getUpgradeUnitClass( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getWithdrawalProbability( self ) :
		# type: () -> int
		pass
	def getWorkRate( self ) :
		# type: () -> int
		pass
	def getXPValueAttack( self ) :
		# type: () -> int
		pass
	def getXPValueDefense( self ) :
		# type: () -> int
		pass
	def isAlwaysHostile( self ) :
		# type: () -> bool
		pass
	def isAnimal( self ) :
		# type: () -> bool
		pass
	def isCanMoveAllTerrain( self ) :
		# type: () -> bool
		pass
	def isCanMoveImpassable( self ) :
		# type: () -> bool
		pass
	def isCounterSpy( self ) :
		# type: () -> bool
		pass
	def isDestroy( self ) :
		# type: () -> bool
		pass
	def isFirstStrikeImmune( self ) :
		# type: () -> bool
		pass
	def isFlatMovementCost( self ) :
		# type: () -> bool
		pass
	def isFoodProduction( self ) :
		# type: () -> bool
		pass
	def isFound( self ) :
		# type: () -> bool
		pass
	def isGoldenAge( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isHiddenNationality( self ) :
		# type: () -> bool
		pass
	def isIgnoreBuildingDefense( self ) :
		# type: () -> bool
		pass
	def isIgnoreTerrainCost( self ) :
		# type: () -> bool
		pass
	def isInvestigate( self ) :
		# type: () -> bool
		pass
	def isInvisible( self ) :
		# type: () -> bool
		pass
	def isLineOfSight( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isMechUnit( self ) :
		# type: () -> bool
		pass
	def isMilitaryHappiness( self ) :
		# type: () -> bool
		pass
	def isMilitaryProduction( self ) :
		# type: () -> bool
		pass
	def isMilitarySupport( self ) :
		# type: () -> bool
		pass
	def isNoBadGoodies( self ) :
		# type: () -> bool
		pass
	def isNoCapture( self ) :
		# type: () -> bool
		pass
	def isNoDefensiveBonus( self ) :
		# type: () -> bool
		pass
	def isNukeImmune( self ) :
		# type: () -> bool
		pass
	def isPillage( self ) :
		# type: () -> bool
		pass
	def isPrereqBonuses( self ) :
		# type: () -> bool
		pass
	def isPrereqReligion( self ) :
		# type: () -> bool
		pass
	def isRenderBelowWater( self ) :
		# type: () -> bool
		pass
	def isRivalTerritory( self ) :
		# type: () -> bool
		pass
	def isSabotage( self ) :
		# type: () -> bool
		pass
	def isSpy( self ) :
		# type: () -> bool
		pass
	def isStealPlans( self ) :
		# type: () -> bool
		pass
	def isSuicide( self ) :
		# type: () -> bool
		pass
	def setCombat( self, arg0 ) :
		# type: (int) -> None
		pass
	def setInvisible( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass

class CvUpkeepInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCityPercent( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getPopulationPercent( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvVictoryInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCityCulture( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getLandPercent( self ) :
		# type: () -> int
		pass
	def getMinLandPercent( self ) :
		# type: () -> int
		pass
	def getMovie( self ) :
		# type: () -> str
		pass
	def getNumCultureCities( self ) :
		# type: () -> int
		pass
	def getPopulationPercentLead( self ) :
		# type: () -> int
		pass
	def getReligionPercent( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTotalCultureRatio( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getVictoryDelayTurns( self ) :
		# type: () -> int
		pass
	def isConquest( self ) :
		# type: () -> bool
		pass
	def isDiploVote( self ) :
		# type: () -> bool
		pass
	def isEndScore( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isPermanent( self ) :
		# type: () -> bool
		pass
	def isTargetScore( self ) :
		# type: () -> bool
		pass

class CvVoteInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getMinVoters( self ) :
		# type: () -> int
		pass
	def getPopulationThreshold( self ) :
		# type: () -> int
		pass
	def getStateReligionVotePercent( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTradeRoutes( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isAssignCity( self ) :
		# type: () -> bool
		pass
	def isCityVoting( self ) :
		# type: () -> bool
		pass
	def isCivVoting( self ) :
		# type: () -> bool
		pass
	def isDefensivePact( self ) :
		# type: () -> bool
		pass
	def isForceCivic( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isForceNoTrade( self ) :
		# type: () -> bool
		pass
	def isForcePeace( self ) :
		# type: () -> bool
		pass
	def isForceWar( self ) :
		# type: () -> bool
		pass
	def isFreeTrade( self ) :
		# type: () -> bool
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass
	def isNoNukes( self ) :
		# type: () -> bool
		pass
	def isOpenBorders( self ) :
		# type: () -> bool
		pass
	def isSecretaryGeneral( self ) :
		# type: () -> bool
		pass
	def isVictory( self ) :
		# type: () -> bool
		pass
	def isVoteSourceType( self, arg0 ) :
		# type: (int) -> bool
		pass

class CvVoteSourceInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivic( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getFreeSpecialist( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getReligionCommerce( self, arg0 ) :
		# type: (int) -> int
		pass
	def getReligionYield( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSecretaryGeneralText( self ) :
		# type: () -> unicode
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getVoteInterval( self ) :
		# type: () -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvWorldInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getBuildingClassPrereqModifier( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getColonyMaintenancePercent( self ) :
		# type: () -> int
		pass
	def getCorporationMaintenancePercent( self ) :
		# type: () -> int
		pass
	def getDefaultPlayers( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getDistanceMaintenancePercent( self ) :
		# type: () -> int
		pass
	def getFeatureGrainChange( self ) :
		# type: () -> int
		pass
	def getGridHeight( self ) :
		# type: () -> int
		pass
	def getGridWidth( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getMaxConscriptModifier( self ) :
		# type: () -> int
		pass
	def getNumCitiesAnarchyPercent( self ) :
		# type: () -> int
		pass
	def getNumCitiesMaintenancePercent( self ) :
		# type: () -> int
		pass
	def getNumFreeBuildingBonuses( self ) :
		# type: () -> int
		pass
	def getResearchPercent( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getTargetNumCities( self ) :
		# type: () -> int
		pass
	def getTerrainGrainChange( self ) :
		# type: () -> int
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTradeProfitPercent( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def getUnitNameModifier( self ) :
		# type: () -> int
		pass
	def getWarWearinessModifier( self ) :
		# type: () -> int
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CvYieldInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAIWeightPercent( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getChar( self ) :
		# type: () -> int
		pass
	def getCityChange( self ) :
		# type: () -> int
		pass
	def getCivilopedia( self ) :
		# type: () -> unicode
		pass
	def getColorType( self ) :
		# type: () -> int
		pass
	def getDescription( self ) :
		# type: () -> unicode
		pass
	def getDescriptionForm( self ) :
		# type: () -> unicode
		pass
	def getGoldenAgeYield( self ) :
		# type: () -> int
		pass
	def getGoldenAgeYieldThreshold( self ) :
		# type: () -> int
		pass
	def getHelp( self ) :
		# type: () -> unicode
		pass
	def getHillsChange( self ) :
		# type: () -> int
		pass
	def getLakeChange( self ) :
		# type: () -> int
		pass
	def getMinCity( self ) :
		# type: () -> int
		pass
	def getPeakChange( self ) :
		# type: () -> int
		pass
	def getPopulationChangeDivisor( self ) :
		# type: () -> int
		pass
	def getPopulationChangeOffset( self ) :
		# type: () -> int
		pass
	def getStrategy( self ) :
		# type: () -> unicode
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def getTextKey( self ) :
		# type: () -> unicode
		pass
	def getTradeModifier( self ) :
		# type: () -> int
		pass
	def getType( self ) :
		# type: () -> str
		pass
	def isGraphicalOnly( self ) :
		# type: () -> bool
		pass
	def isMatchForLink( self, arg0 ) :
		# type: (str) -> bool
		pass

class CyArea( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def calculateTotalBestNatureYield( self ) :
		# type: () -> int
		""" Returns the total tile yield from the area """
	def countCoastalLand( self, *args, **kwargs ) :
		pass
	def countHasCorporation( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def countHasReligion( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def countNumUniqueBonusTypes( self ) :
		# type: () -> int
		""" Returns the number of unique bonus types in this area """
	def getAnimalsPerPlayer( self, arg0 ) :
		# type: (int) -> int
		""" Returns the number of animal units in this area for this player """
	def getAreaAIType( self, arg0 ) :
		# type: (int) -> int
		""" Returns the AreaAIType for this team in this area """
	def getBestFoundValue( self, arg0 ) :
		# type: (int) -> int
		""" Returns the best found value for a plot in this area """
	def getBuildingBadHealth( self, arg0 ) :
		# type: (int) -> int
		""" Returns ? """
	def getBuildingGoodHealth( self, arg0 ) :
		# type: (int) -> int
		""" Returns ? """
	def getBuildingHappiness( self, arg0 ) :
		# type: (int) -> int
		""" Returns ? """
	def getCitiesPerPlayer( self, arg0 ) :
		# type: (int) -> int
		""" Returns the number of cities in this area for this player """
	def getFreeSpecialist( self, arg0 ) :
		# type: (int) -> int
		""" Returns ? """
	def getID( self ) :
		# type: () -> int
		""" Return's the Areas ID """
	def getNumAIUnits( self, arg0, arg1 ) :
		# type: (int, int) -> int
		""" Returns the number of units for this AI which have this AI type """
	def getNumBonuses( self, BonusID ) :
		# type: (Any) -> int
		""" total # of BonusID """
	def getNumCities( self ) :
		# type: () -> int
		""" Returns the total number of cities for all players in this area """
	def getNumImprovements( self, ImprovementID ) :
		# type: (Any) -> int
		""" total # of ImprovementID """
	def getNumOwnedTiles( self ) :
		# type: () -> int
		""" Returns the number of owned tiles in this area """
	def getNumRevealedTiles( self, arg0 ) :
		# type: (int) -> int
		""" Returns the number of revealed tiles for this team """
	def getNumRiverEdges( self ) :
		# type: () -> int
		""" Returns the number of River Edges in this area """
	def getNumStartingPlots( self ) :
		# type: () -> int
		""" total number of players that are starting on this area """
	def getNumTiles( self ) :
		# type: () -> int
		""" Returns the number of tiles in this area """
	def getNumTotalBonuses( self ) :
		# type: () -> int
		""" total number of bonuses, of all types """
	def getNumTrainAIUnits( self, arg0, arg1 ) :
		# type: (int, int) -> int
		""" Returns ? """
	def getNumUnits( self ) :
		# type: () -> int
		""" Returns the total number of units for all players in this area """
	def getNumUnownedTiles( self ) :
		# type: () -> int
		""" Returns the number of unowned tiles in this area """
	def getNumUnrevealedTiles( self, arg0 ) :
		# type: (int) -> int
		""" Returns the number of unrevealed tiles for this team """
	def getPopulationPerPlayer( self, arg0 ) :
		# type: (int) -> int
		""" Returns the total population of this area for this player """
	def getPower( self, arg0 ) :
		# type: (int) -> int
		""" Returns power of this area for this player """
	def getTargetCity( self, arg0 ) :
		# type: (int) -> CyCity
		""" Returns ? """
	def getTotalPopulation( self ) :
		# type: () -> int
		""" Returns the total population for all players in this area """
	def getUnitsPerPlayer( self, arg0 ) :
		# type: (int) -> int
		""" Returns the number of units in this area for this player """
	def getYieldRateModifier( self, *args, **kwargs ) :
		""" int (int (PlayerTypes) iPlayer, int (YieldTypes) iIndex2 - Returns ? """
	def isBorderObstacle( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isCleanPower( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isLake( self ) :
		# type: () -> bool
		""" Returns whether the area is a fresh water lake """
	def isNone( self ) :
		# type: () -> bool
		""" Returns whether the pointer points to a real Area """
	def isWater( self ) :
		# type: () -> bool
		""" Returns whether or not this area is water """

class CyArtFileMgr( object ) :
	def Reset( self ) :
		# type: () -> None
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	def buildArtFileInfoMaps( self ) :
		# type: () -> None
		pass
	def getBonusArtInfo( self ) :
		# type: () -> CvArtInfoBonus
		pass
	def getBuildingArtInfo( self ) :
		# type: () -> CvArtInfoBuilding
		pass
	def getCivilizationArtInfo( self ) :
		# type: () -> CvArtInfoCivilization
		pass
	def getFeatureArtInfo( self ) :
		# type: () -> CvArtInfoFeature
		pass
	def getImprovementArtInfo( self ) :
		# type: () -> CvArtInfoImprovement
		pass
	def getInterfaceArtInfo( self ) :
		# type: () -> CvArtInfoInterface
		pass
	def getLeaderheadArtInfo( self ) :
		# type: () -> CvArtInfoLeaderhead
		pass
	def getMiscArtInfo( self ) :
		# type: () -> CvArtInfoMisc
		pass
	def getMovieArtInfo( self ) :
		# type: () -> CvArtInfoMovie
		pass
	def getTerrainArtInfo( self ) :
		# type: () -> CvArtInfoTerrain
		pass
	def getUnitArtInfo( self ) :
		# type: () -> CvArtInfoUnit
		pass
	def isNone( self ) :
		# type: () -> bool
		""" Checks to see if pointer points to a real object """

class CyAudioGame( object ) :
	def Destroy2DSound( self, arg0 ) :
		# type: (int) -> None
		""" Stop playing and destroy sound using soundhandle. """
	def Destroy3DSound( self, arg0 ) :
		# type: (int) -> None
		""" Stop playing and destroy sound using soundhandle. """
	def Is2DSoundPlaying( self, arg0 ) :
		# type: (int) -> bool
		""" Is the sound using this soundhandle and scriptname playing?. """
	def Is3DSoundPlaying( self, arg0 ) :
		# type: (int) -> bool
		""" Is the sound using this soundhandle and scriptname playing?. """
	def Play2DSound( self, arg0 ) :
		# type: (str) -> int
		""" Play 2d sound using scriptname and return a handle to the sound. """
	def Play2DSoundWithId( self, arg0 ) :
		# type: (int) -> int
		""" Play 2d sound using scriptId and return a handle to the sound. """
	def Play3DSound( self, arg0, arg1, arg2, arg3 ) :
		# type: (str, float, float, float) -> int
		""" Play 3d sound using scriptname at position (x,y,z) and return a handle to the sound. """
	def Play3DSoundWithId( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, float, float, float) -> int
		""" Play 3d sound using scriptId at position (x,y,z) and return a handle to the sound. """
	def Set2DSoundVolume( self, arg0, arg1 ) :
		# type: (int, float) -> None
		""" Set volume to value between 0.0f and 1.0f to sound using soundhandle. """
	def Set3DSoundPosition( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, float, float, float) -> None
		""" Set position of sound using soundhandle to (x,y,z). """
	def Set3DSoundVolume( self, arg0, arg1 ) :
		# type: (int, float) -> None
		""" Set volume to value between 0.0f and 1.0f to sound using soundhandle. """
	def __init__( self, *args, **kwargs ) :
		pass

class CyCamera( object ) :
	def GetBasePitch( self ) :
		# type: () -> float
		pass
	def GetBaseTurn( self ) :
		# type: () -> float
		pass
	def GetCameraMovementSpeed( self ) :
		# type: () -> float
		pass
	def GetCurrentPosition( self ) :
		# type: () -> NiPoint3
		pass
	def GetDefaultViewPortCenter( self, *args, **kwargs ) :
		""" NiPoint2 CyCamera().GetDefaultViewPortCenter() """
	def GetDestinationPosition( self ) :
		# type: () -> NiPoint3
		pass
	def GetLookAt( self, arg0 ) :
		# type: (NiPoint3) -> None
		pass
	def GetLookAtSpeed( self ) :
		# type: () -> float
		pass
	def GetTargetDestination( self ) :
		# type: () -> NiPoint3
		pass
	def GetZoom( self ) :
		# type: () -> float
		pass
	def JustLookAt( self, *args, **kwargs ) :
		""" void (CyPlot().getPoint()) - centers on plot """
	def JustLookAtPlot( self, arg0 ) :
		# type: (CyPlot) -> None
		""" centers on plot """
	def LookAt( self, arg0, arg1, arg2 ) :
		# type: (NiPoint3, int, NiPoint3) -> None
		""" centers the camera on the point """
	def LookAtUnit( self, arg0 ) :
		# type: (CyUnit) -> None
		""" follow a unit """
	def MoveBaseTurnLeft( self, arg0 ) :
		# type: (float) -> None
		pass
	def MoveBaseTurnRight( self, arg0 ) :
		# type: (float) -> None
		pass
	def ReleaseLockedCamera( self ) :
		# type: () -> None
		pass
	def ResetZoom( self ) :
		# type: () -> None
		pass
	def SetBasePitch( self, arg0 ) :
		# type: (float) -> None
		pass
	def SetBaseTurn( self, arg0 ) :
		# type: (float) -> None
		pass
	def SetCameraMovementSpeed( self, arg0 ) :
		# type: (int) -> None
		pass
	def SetCurrentPosition( self, arg0 ) :
		# type: (NiPoint3) -> None
		pass
	def SetDestinationPosition( self, arg0 ) :
		# type: (NiPoint3) -> None
		pass
	def SetLookAtSpeed( self, arg0 ) :
		# type: (float) -> None
		pass
	def SetTargetDestination( self, arg0 ) :
		# type: (NiPoint3) -> None
		pass
	def SetViewPortCenter( self, arg0 ) :
		# type: (NiPoint2) -> None
		pass
	def SetZoom( self, *args, **kwargs ) :
		""" void (float zoom=0.5) """
	def SimpleLookAt( self, arg0, arg1 ) :
		# type: (NiPoint3, NiPoint3) -> None
		""" moves the camera to position looking at target """
	def Translate( self, *args, **kwargs ) :
		""" void (NiPoint3 translation=(fX, fY, fZ) """
	def ZoomIn( self, *args, **kwargs ) :
		""" void (float increment=0.5) """
	def ZoomOut( self, arg0 ) :
		# type: (float) -> None
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	def isMoving( self ) :
		# type: () -> bool
		pass
	def setOrthoCamera( self, arg0 ) :
		# type: (bool) -> None
		pass

class CyCity( object ) :
	def AI_avoidGrowth( self ) :
		# type: () -> bool
		pass
	def AI_cityValue( self ) :
		# type: () -> int
		pass
	def AI_countBestBuilds( self, arg0 ) :
		# type: (CyArea) -> int
		pass
	def AI_isEmphasize( self, arg0 ) :
		# type: (int) -> bool
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	def addProductionExperience( self, arg0, arg1 ) :
		# type: (CyUnit, bool) -> None
		pass
	def allUpgradesAvailable( self, *args, **kwargs ) :
		""" int UnitTypes (int eUnit, int iUpgradeCount) """
	def alterSpecialistCount( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def alterWorkingPlot( self, iIndex ) :
		# type: (Any) -> None
		pass
	def angryPopulation( self, iExtra ) :
		# type: (Any) -> int
		""" # of unhappy citizens """
	def area( self, *args, **kwargs ) :
		""" CyArea() () - returns CyArea instance for location of city """
	def at( self, iX, iY ) :
		# type: (Any, Any) -> bool
		""" is the city at (iX, iY) ? """
	def atPlot( self, arg0 ) :
		# type: (CyPlot) -> bool
		""" is pPlot the cities plot? """
	def badHealth( self, arg0 ) :
		# type: (bool) -> int
		""" total unhealthiness """
	def calculateColonyMaintenance( self ) :
		# type: () -> int
		pass
	def calculateColonyMaintenanceTimes100( self ) :
		# type: () -> int
		pass
	def calculateCorporationMaintenance( self ) :
		# type: () -> int
		pass
	def calculateCorporationMaintenanceTimes100( self ) :
		# type: () -> int
		pass
	def calculateCulturePercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def calculateDistanceMaintenance( self ) :
		# type: () -> int
		pass
	def calculateDistanceMaintenanceTimes100( self ) :
		# type: () -> int
		pass
	def calculateNumCitiesMaintenance( self ) :
		# type: () -> int
		pass
	def calculateNumCitiesMaintenanceTimes100( self ) :
		# type: () -> int
		pass
	def calculateTeamCulturePercent( self ) :
		# type: () -> int
		pass
	def calculateTradeProfit( self, arg0 ) :
		# type: (CyCity) -> int
		""" returns the trade profit created by CyCity """
	def calculateTradeYield( self, YieldType, arg1 ) :
		# type: (Any, int) -> int
		""" calculates Trade Yield """
	def canConscript( self ) :
		# type: () -> bool
		""" can the city conscript units? """
	def canConstruct( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, bool, bool, bool) -> bool
		pass
	def canContinueProduction( self, arg0 ) :
		# type: (OrderData) -> bool
		pass
	def canCreate( self, arg0, arg1, arg2 ) :
		# type: (int, bool, bool) -> bool
		pass
	def canHurry( self, *args, **kwargs ) :
		""" bool (HurryTypes eHurry, bool bTestVisible = 0) - can player eHurry in this city? """
	def canJoin( self ) :
		# type: () -> bool
		""" can a Great Person join the city """
	def canMaintain( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def canTrain( self, arg0, arg1, arg2 ) :
		# type: (int, bool, bool) -> bool
		pass
	def canWork( self, arg0 ) :
		# type: (CyPlot) -> bool
		""" can the city work the plot? """
	def changeBaseGreatPeopleRate( self, *args, **kwargs ) :
		pass
	def changeBaseYieldRate( self, arg0, arg1 ) :
		# type: (int, int) -> int
		""" changes the base rate for YieldType """
	def changeBuildingProduction( self, BuildingID, iChange ) :
		# type: (Any, Any) -> None
		""" adjusts progress towards BuildingID by iChange """
	def changeBuildingProductionTime( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def changeConscriptAngerTimer( self, arg0 ) :
		# type: (int) -> None
		""" changes the amount of time left on the conscript anger timer """
	def changeCulture( self, *args, **kwargs ) :
		""" void (int PlayerTypes eIndex, int iChange, bool bPlots) """
	def changeCultureTimes100( self, *args, **kwargs ) :
		""" void (int PlayerTypes eIndex, int iChange, bool bPlots) """
	def changeCultureUpdateTimer( self, iChange ) :
		# type: (Any) -> None
		""" adjusts the Culture Update Timer by iChange """
	def changeDefenseDamage( self, iChange ) :
		# type: (Any) -> None
		""" adjust damage value by iChange """
	def changeDefyResolutionAngerTimer( self, arg0 ) :
		# type: (int) -> None
		""" changes the amount of time left on the anger timer """
	def changeEspionageHappinessCounter( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeEspionageHealthCounter( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeExtraHappiness( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeExtraHealth( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeExtraTradeRoutes( self, iChange ) :
		# type: (Any) -> None
		""" Change the number of trade routes this city has """
	def changeFood( self, iChange ) :
		# type: (Any) -> None
		""" adjust stored food by iChange """
	def changeForceSpecialistCount( self, *args, **kwargs ) :
		""" int (int /*SpecialistTypes*/ eIndex, int iChange """
	def changeFreeBonus( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeFreeSpecialistCount( self, *args, **kwargs ) :
		""" int (int /*SpecialistTypes*/ eIndex, iChange """
	def changeGreatPeopleProgress( self, arg0 ) :
		# type: (int) -> None
		""" adjusts great person progress by iChange """
	def changeGreatPeopleUnitProgress( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def changeHappinessTimer( self, iChange ) :
		# type: (Any) -> None
		""" adjust Happiness timer by iChange """
	def changeHealRate( self, arg0 ) :
		# type: (int) -> None
		""" changes the heal rate of this city to iChange """
	def changeHurryAngerTimer( self, iChange ) :
		# type: (Any) -> None
		""" adjust Hurry Angry timer by iChange """
	def changeImprovementFreeSpecialists( self, ImprovementID, iChange ) :
		# type: (Any, Any) -> None
		""" adjust ImprovementID free specialists by iChange """
	def changeNoBonusCount( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeOccupationTimer( self, iChange ) :
		# type: (Any) -> None
		""" adjusts the Occupation Timer by iChange """
	def changePopulation( self, arg0 ) :
		# type: (int) -> None
		""" adjusts the city population by iChange """
	def changeProduction( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeReligionInfluence( self, ReligionID, iChange ) :
		# type: (Any, Any) -> None
		""" adjust ReligionID influence by iChange """
	def changeSpecialistCommerce( self, arg0, iChange ) :
		# type: (int, Any) -> None
		""" adjusts Specialist contribution to CommerceType by iChange """
	def changeStateReligionHappiness( self, arg0, iChange ) :
		# type: (int, Any) -> None
		pass
	def changeUnitProduction( self, UnitID, iChange ) :
		# type: (Any, Any) -> None
		""" adjusts production towards UnitID by iChange """
	def chooseProduction( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, int, int, bool, bool) -> None
		""" Chooses production for a city """
	def clearOrderQueue( self ) :
		# type: () -> None
		pass
	def clearWorkingOverride( self, arg0 ) :
		# type: (int) -> None
		pass
	def conscript( self ) :
		# type: () -> None
		""" conscripts a unit """
	def conscriptMinCityPopulation( self ) :
		# type: () -> int
		pass
	def countNumImprovedPlots( self ) :
		# type: () -> int
		pass
	def countNumRiverPlots( self ) :
		# type: () -> int
		pass
	def countNumWaterPlots( self ) :
		# type: () -> int
		pass
	def countTotalCultureTimes100( self ) :
		# type: () -> int
		pass
	def createGreatPeople( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		""" Creates a great person in this city and whether it should increment the threshold to the next level """
	def cultureDistance( self, iDX, iDY ) :
		# type: (Any, Any) -> int
		""" culture distance """
	def cultureGarrison( self, ePlayer ) :
		# type: (Any) -> int
		pass
	def cultureStrength( self, ePlayer ) :
		# type: (Any) -> int
		pass
	def doTask( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, int, bool) -> None
		""" Enacts the TaskType passed """
	def extraFreeSpecialists( self ) :
		# type: () -> int
		""" # of specialist that are allowed for free """
	def extraPopulation( self ) :
		# type: () -> int
		""" # of extra/available citizens """
	def extraSpecialists( self ) :
		# type: () -> int
		""" # of extra/available specialists """
	def findBaseYieldRateRank( self, arg0 ) :
		# type: (int) -> int
		pass
	def findCommerceRateRank( self, arg0 ) :
		# type: (int) -> int
		pass
	def findHighestCulture( self ) :
		# type: () -> int
		pass
	def findPopulationRank( self ) :
		# type: () -> int
		pass
	def findYieldRateRank( self, arg0 ) :
		# type: (int) -> int
		pass
	def flatConscriptAngerLength( self ) :
		# type: () -> int
		pass
	def flatDefyResolutionAngerLength( self ) :
		# type: () -> int
		pass
	def flatHurryAngerLength( self ) :
		# type: () -> int
		pass
	def foodConsumption( self, arg0, arg1 ) :
		# type: (bool, int) -> int
		pass
	def foodDifference( self, arg0 ) :
		# type: (bool) -> int
		""" result of getYieldRate(Food) - foodConsumption() """
	def getAddedFreeSpecialistCount( self, *args, **kwargs ) :
		""" int (int /*SpecialistTypes*/ eIndex """
	def getAirModifier( self ) :
		# type: () -> int
		""" returns the air defense modifier """
	def getAirUnitCapacity( self, arg0 ) :
		# type: (int) -> int
		""" returns the number of air units allowed here """
	def getArtStyleType( self ) :
		# type: () -> int
		pass
	def getBaseCommerceRate( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBaseCommerceRateTimes100( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBaseGreatPeopleRate( self ) :
		# type: () -> int
		""" base great person rate """
	def getBaseYieldRate( self, arg0 ) :
		# type: (int) -> int
		""" base rate for YieldType """
	def getBaseYieldRateModifier( self, *args, **kwargs ) :
		pass
	def getBonusBadHealth( self ) :
		# type: () -> int
		pass
	def getBonusGoodHappiness( self ) :
		# type: () -> int
		pass
	def getBonusGoodHealth( self ) :
		# type: () -> int
		pass
	def getBonusHappiness( self, BonusID ) :
		# type: (Any) -> int
		""" total happiness bonus from BonusID """
	def getBonusHealth( self, BonusID ) :
		# type: (Any) -> int
		""" total health bonus from BonusID """
	def getBonusPower( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def getBonusYieldRateModifier( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getBuildingBadHappiness( self ) :
		# type: () -> int
		pass
	def getBuildingBadHealth( self ) :
		# type: () -> int
		pass
	def getBuildingBombardDefense( self ) :
		# type: () -> int
		""" building defense """
	def getBuildingCommerce( self, arg0 ) :
		# type: (int) -> int
		""" total effect of cities buildings on CommerceTypes """
	def getBuildingCommerceByBuilding( self, arg0, arg1 ) :
		# type: (int, int) -> int
		""" total value of CommerceType from BuildingTypes """
	def getBuildingCommerceChange( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getBuildingDefense( self ) :
		# type: () -> int
		""" building defense """
	def getBuildingGoodHappiness( self ) :
		# type: () -> int
		pass
	def getBuildingGoodHealth( self ) :
		# type: () -> int
		pass
	def getBuildingHappiness( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingHappyChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingHealth( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingHealthChange( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingOriginalOwner( self, BuildingType ) :
		# type: (Any) -> int
		""" index of original building owner """
	def getBuildingOriginalTime( self, BuildingType ) :
		# type: (Any) -> int
		""" original build date """
	def getBuildingProduction( self, BuildingID ) :
		# type: (Any) -> int
		""" current production towards BuildingID """
	def getBuildingProductionModifier( self, BuildingID ) :
		# type: (Any) -> int
		""" production multiplier for BuildingID """
	def getBuildingProductionTime( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingProductionTurnsLeft( self, BuildingID, arg1 ) :
		# type: (Any, int) -> int
		""" # of turns remaining to complete UnitID """
	def getBuildingYieldChange( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getCityIndexPlot( self, arg0 ) :
		# type: (int) -> CyPlot
		pass
	def getCityPlotIndex( self, arg0 ) :
		# type: (CyPlot) -> int
		pass
	def getCitySizeType( self ) :
		# type: () -> int
		pass
	def getCivilizationType( self ) :
		# type: () -> CivilizationID
		""" owners CivilizationID """
	def getCommerceFromPercent( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getCommerceHappiness( self ) :
		# type: () -> int
		""" happiness from all CommerceTypes """
	def getCommerceHappinessByType( self, arg0 ) :
		# type: (int) -> int
		""" happiness from CommerceType """
	def getCommerceHappinessPer( self, arg0 ) :
		# type: (int) -> int
		""" happiness from each level of entertainment """
	def getCommerceRate( self, arg0 ) :
		# type: (int) -> int
		""" total Commerce rate """
	def getCommerceRateModifier( self, arg0 ) :
		# type: (int) -> int
		""" indicates the total rate modifier on CommerceType """
	def getCommerceRateTimes100( self, arg0 ) :
		# type: (int) -> int
		""" total Commerce rate """
	def getConscriptAngerTimer( self ) :
		# type: () -> int
		""" returns the amount of time left on the conscript anger timer """
	def getConscriptPopulation( self ) :
		# type: () -> int
		pass
	def getConscriptUnit( self ) :
		# type: () -> UnitID
		""" UnitID for the best unit the city can conscript """
	def getCorporationCommerce( self, arg0 ) :
		# type: (int) -> int
		""" effect on CommerceType by Corporation """
	def getCorporationCommerceByCorporation( self, arg0, CorporationType ) :
		# type: (int, Any) -> int
		""" CommerceType effect from CorporationType """
	def getCorporationYield( self, arg0 ) :
		# type: (int) -> int
		""" effect on YieldTypes by Corporation """
	def getCorporationYieldByCorporation( self, arg0, CorporationType ) :
		# type: (int, Any) -> int
		""" YieldTypes effect from CorporationType """
	def getCulture( self ) :
		# type: () -> int
		pass
	def getCultureLevel( self ) :
		# type: () -> int
		pass
	def getCulturePercentAnger( self ) :
		# type: () -> int
		pass
	def getCultureThreshold( self, *args, **kwargs ) :
		pass
	def getCultureTimes100( self ) :
		# type: () -> int
		pass
	def getCultureUpdateTimer( self ) :
		# type: () -> int
		""" Culture Update Timer """
	def getCurrAirlift( self ) :
		# type: () -> int
		pass
	def getCurrentProductionDifference( self, arg0, arg1 ) :
		# type: (bool, bool) -> int
		pass
	def getCurrentStateReligionHappiness( self ) :
		# type: () -> int
		pass
	def getDefenseDamage( self ) :
		# type: () -> int
		""" value of damage city defenses can receive """
	def getDefenseModifier( self, arg0 ) :
		# type: (bool) -> int
		pass
	def getDefyResolutionAngerTimer( self ) :
		# type: () -> int
		""" returns the amount of time left on the anger timer """
	def getDomainFreeExperience( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDomainProductionModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getEspionageDefenseModifier( self ) :
		# type: () -> int
		pass
	def getEspionageHappinessCounter( self ) :
		# type: () -> int
		pass
	def getEspionageHealthCounter( self ) :
		# type: () -> int
		pass
	def getEspionageVisibility( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getExtraBuildingBadHappiness( self ) :
		# type: () -> int
		pass
	def getExtraBuildingGoodHappiness( self ) :
		# type: () -> int
		pass
	def getExtraHappiness( self ) :
		# type: () -> int
		pass
	def getExtraHealth( self ) :
		# type: () -> int
		pass
	def getExtraProductionDifference( self, arg0 ) :
		# type: (int) -> int
		pass
	def getExtraSpecialistYield( self, arg0 ) :
		# type: (int) -> int
		pass
	def getExtraSpecialistYieldOfType( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getExtraTradeRoutes( self ) :
		# type: () -> int
		""" returns the number of extra trade routes this city has """
	def getFeatureBadHappiness( self ) :
		# type: () -> int
		pass
	def getFeatureBadHealth( self ) :
		# type: () -> int
		""" returns the bad health provided by the feature this city is built on """
	def getFeatureGoodHappiness( self ) :
		# type: () -> int
		pass
	def getFeatureGoodHealth( self ) :
		# type: () -> int
		""" returns the good health provided by the feature this city is built on """
	def getFeatureProduction( self ) :
		# type: () -> int
		""" value of feature production """
	def getFirstBuildingOrder( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFirstProjectOrder( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFirstUnitOrder( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFood( self ) :
		# type: () -> int
		""" stored food """
	def getFoodKept( self ) :
		# type: () -> int
		pass
	def getFoodTurnsLeft( self ) :
		# type: () -> int
		""" how many food turns remain? """
	def getForceSpecialistCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getForeignTradeRouteModifier( self ) :
		# type: () -> int
		pass
	def getFreeBonus( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFreeExperience( self ) :
		# type: () -> int
		""" # of free experience newly trained units receive """
	def getFreePromotionCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFreeSpecialist( self ) :
		# type: () -> int
		pass
	def getFreeSpecialistCount( self, *args, **kwargs ) :
		""" int (int /*SpecialistTypes*/ eIndex """
	def getFreshWaterBadHealth( self ) :
		# type: () -> int
		pass
	def getFreshWaterGoodHealth( self ) :
		# type: () -> int
		pass
	def getGameTurnAcquired( self ) :
		# type: () -> int
		pass
	def getGameTurnFounded( self ) :
		# type: () -> int
		""" GameTurn the city was founded """
	def getGeneralProductionTurnsLeft( self, *args, **kwargs ) :
		""" int - # of production turns left for the top order node item in a city... """
	def getGreatPeopleProgress( self ) :
		# type: () -> int
		""" current great person progress """
	def getGreatPeopleRate( self ) :
		# type: () -> int
		""" total Great Person rate """
	def getGreatPeopleRateModifier( self ) :
		# type: () -> int
		pass
	def getGreatPeopleUnitProgress( self, arg0 ) :
		# type: (int) -> int
		pass
	def getGreatPeopleUnitRate( self, arg0 ) :
		# type: (int) -> int
		pass
	def getHandicapType( self ) :
		# type: () -> HandicapType
		""" owners difficulty level """
	def getHappinessTimer( self ) :
		# type: () -> int
		""" Temporary Happiness timer """
	def getHighestPopulation( self, *args, **kwargs ) :
		""" int ()  """
	def getHurryAngerModifier( self, *args, **kwargs ) :
		pass
	def getHurryAngerTimer( self ) :
		# type: () -> int
		""" Anger caused by Hurrying timer """
	def getID( self ) :
		# type: () -> int
		""" index ID # for the city - use with pPlayer.getCity(ID) to obtain city instance """
	def getImprovementFreeSpecialists( self, ImprovementID ) :
		# type: (Any) -> int
		pass
	def getLargestCityHappiness( self ) :
		# type: () -> int
		pass
	def getLiberationPlayer( self ) :
		# type: () -> int
		pass
	def getMaintenance( self ) :
		# type: () -> int
		""" cities current maintenance cost """
	def getMaintenanceModifier( self ) :
		# type: () -> int
		""" total value of the city maintenance modifier """
	def getMaintenanceTimes100( self ) :
		# type: () -> int
		""" cities current maintenance cost """
	def getMaxAirlift( self ) :
		# type: () -> int
		pass
	def getMaxFoodKeptPercent( self ) :
		# type: () -> int
		pass
	def getMaxSpecialistCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getMilitaryHappiness( self ) :
		# type: () -> int
		""" happiness created by military units stationed in the city """
	def getMilitaryHappinessUnits( self, *args, **kwargs ) :
		""" number of military units creating happiness """
	def getMilitaryProductionModifier( self ) :
		# type: () -> int
		""" value of adjustments to military production """
	def getName( self ) :
		# type: () -> str
		""" city name """
	def getNameForm( self ) :
		# type: () -> str
		""" city name """
	def getNameKey( self ) :
		# type: () -> str
		""" city name """
	def getNaturalDefense( self ) :
		# type: () -> int
		pass
	def getNoMilitaryPercentAnger( self ) :
		# type: () -> int
		pass
	def getNukeModifier( self ) :
		# type: () -> int
		pass
	def getNumActiveBuilding( self, BuildingID ) :
		# type: (Any) -> bool
		""" is BuildingID active in the city (present & not obsolete)? """
	def getNumBonuses( self, PlayerID ) :
		# type: (Any) -> int
		pass
	def getNumBuilding( self, *args, **kwargs ) :
		""" int - (BuildingID) - How many BuildingID does this city have (real or free)? """
	def getNumBuildings( self ) :
		# type: () -> int
		pass
	def getNumFreeBuilding( self, BuildingID ) :
		# type: (Any) -> int
		""" # of free Building ID (ie: from a Wonder) """
	def getNumGreatPeople( self ) :
		# type: () -> int
		""" # of great people who are joined to the city """
	def getNumNationalWonders( self ) :
		# type: () -> int
		pass
	def getNumRealBuilding( self, BuildingID ) :
		# type: (Any) -> int
		""" get # real building of this type """
	def getNumTeamWonders( self ) :
		# type: () -> int
		pass
	def getNumWorldWonders( self ) :
		# type: () -> int
		pass
	def getOccupationTimer( self ) :
		# type: () -> int
		""" total # of turns remaining on occupation timer """
	def getOrderFromQueue( self, arg0 ) :
		# type: (int) -> OrderData
		pass
	def getOrderQueueLength( self ) :
		# type: () -> None
		pass
	def getOriginalOwner( self ) :
		# type: () -> int
		pass
	def getOvercrowdingPercentAnger( self, iExtra ) :
		# type: (Any) -> int
		pass
	def getOverflowProduction( self ) :
		# type: () -> int
		""" value of overflow production """
	def getOwner( self ) :
		# type: () -> int
		pass
	def getPersonalityType( self ) :
		# type: () -> int
		pass
	def getPopulation( self ) :
		# type: () -> int
		""" total city population """
	def getPowerBadHealth( self ) :
		# type: () -> int
		pass
	def getPowerGoodHealth( self ) :
		# type: () -> int
		pass
	def getPreviousOwner( self ) :
		# type: () -> int
		pass
	def getProduction( self ) :
		# type: () -> int
		""" returns the current production towards whatever is top of this city's OrderQueue """
	def getProductionBuilding( self ) :
		# type: () -> BuildingID
		""" ID for building that is under construction """
	def getProductionExperience( self, arg0 ) :
		# type: (int) -> int
		pass
	def getProductionModifier( self ) :
		# type: () -> int
		""" multiplier (if any) for item being produced """
	def getProductionName( self ) :
		# type: () -> str
		""" description of item that the city is working on """
	def getProductionNameKey( self ) :
		# type: () -> str
		""" description of item that the city is working on """
	def getProductionNeeded( self ) :
		# type: () -> int
		""" # of production needed to complete construction """
	def getProductionProcess( self ) :
		# type: () -> int
		pass
	def getProductionProject( self ) :
		# type: () -> int
		pass
	def getProductionToCommerceModifier( self, arg0 ) :
		# type: (int) -> int
		""" value of production to commerce modifier """
	def getProductionTurnsLeft( self ) :
		# type: () -> int
		""" # of turns remaining until item is completed """
	def getProductionUnit( self ) :
		# type: () -> UnitID
		""" ID for unit that is being trained """
	def getProductionUnitAI( self, *args, **kwargs ) :
		""" int eUnitAIType () """
	def getProjectProductionModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getProjectProductionTurnsLeft( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getRallyPlot( self ) :
		# type: () -> CyPlot
		""" returns city's rally plot instance """
	def getRealPopulation( self ) :
		# type: () -> int
		""" total city population in "real" numbers """
	def getReligionBadHappiness( self ) :
		# type: () -> int
		pass
	def getReligionCommerce( self, arg0 ) :
		# type: (int) -> int
		""" effect on CommerceType by Religions """
	def getReligionCommerceByReligion( self, arg0, ReligionType ) :
		# type: (int, Any) -> int
		""" CommerceType effect from ReligionType """
	def getReligionGoodHappiness( self ) :
		# type: () -> int
		pass
	def getReligionHappiness( self, arg0 ) :
		# type: (int) -> int
		pass
	def getReligionInfluence( self, ReligionID ) :
		# type: (Any) -> int
		""" value of influence from ReligionID """
	def getReligionPercentAnger( self ) :
		# type: () -> int
		pass
	def getRiverPlotYield( self, arg0 ) :
		# type: (int) -> int
		""" total YieldType for river plots """
	def getScriptData( self ) :
		# type: () -> str
		""" Get stored custom data (via pickle) """
	def getSeaPlotYield( self, arg0 ) :
		# type: (int) -> int
		""" total YieldType for water plots """
	def getSpaceProductionModifier( self ) :
		# type: () -> int
		pass
	def getSpecialistCommerce( self, arg0 ) :
		# type: (int) -> int
		""" value of CommerceType adjustment from Specialists """
	def getSpecialistCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSpecialistFreeExperience( self ) :
		# type: () -> int
		pass
	def getSpecialistPopulation( self ) :
		# type: () -> int
		""" # of specialists """
	def getStateReligionHappiness( self, arg0 ) :
		# type: (int) -> int
		pass
	def getTeam( self ) :
		# type: () -> int
		pass
	def getTotalCommerceRateModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getTotalDefense( self, arg0 ) :
		# type: (bool) -> int
		pass
	def getTotalGreatPeopleRateModifier( self ) :
		# type: () -> int
		pass
	def getTradeCity( self, arg0 ) :
		# type: (int) -> CyCity
		""" remove SpecialistType[iIndex] """
	def getTradeRouteModifier( self ) :
		# type: () -> int
		pass
	def getTradeRoutes( self ) :
		# type: () -> int
		pass
	def getTradeYield( self, arg0 ) :
		# type: (int) -> int
		""" trade adjustment to YieldType """
	def getUnitCombatFreeExperience( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitProduction( self, UnitID ) :
		# type: (Any) -> int
		""" gets current production towards UnitID """
	def getUnitProductionModifier( self, UnitID ) :
		# type: (Any) -> int
		""" production multiplier for UnitID """
	def getUnitProductionTurnsLeft( self, UnitID, arg1 ) :
		# type: (Any, int) -> int
		""" # of turns remaining to complete UnitID """
	def getWallOverridePoints( self ) :
		# type: () -> Tuple
		pass
	def getWarWearinessModifier( self, *args, **kwargs ) :
		pass
	def getWarWearinessPercentAnger( self ) :
		# type: () -> int
		pass
	def getWorkingPopulation( self ) :
		# type: () -> int
		""" # of citizens who are working """
	def getX( self ) :
		# type: () -> int
		""" X coordinate for the cities plot """
	def getY( self ) :
		# type: () -> int
		""" Y coordinate for the cities plot """
	def getYieldRate( self, arg0 ) :
		# type: (int) -> int
		""" total value of YieldType """
	def getYieldRateModifier( self, arg0 ) :
		# type: (int) -> int
		""" yield rate modifier for YieldType """
	def goodHealth( self ) :
		# type: () -> int
		""" total health """
	def growthThreshold( self ) :
		# type: () -> int
		""" value needed for growth """
	def happyLevel( self ) :
		# type: () -> int
		pass
	def hasBonus( self, *args, **kwargs ) :
		""" bool - (BonusID) - is BonusID connected to the city? """
	def hasTrait( self, TraitID ) :
		# type: (Any) -> bool
		""" does owner have TraitID? """
	def healthRate( self, arg0, arg1 ) :
		# type: (bool, int) -> int
		pass
	def hurry( self, arg0 ) :
		# type: (int) -> None
		""" forces the city to rush production using eHurry """
	def hurryAngerLength( self, HurryID ) :
		# type: (Any) -> int
		pass
	def hurryCost( self, arg0 ) :
		# type: (bool) -> int
		pass
	def hurryGold( self, HurryID ) :
		# type: (Any) -> int
		""" total value of gold when hurrying """
	def hurryPopulation( self, HurryID ) :
		# type: (Any) -> int
		""" value of each pop when hurrying """
	def hurryProduction( self, HurryID ) :
		# type: (Any) -> int
		pass
	def isActiveCorporation( self, CorporationID ) :
		# type: (Any) -> bool
		""" does city have active CorporationID? """
	def isAirliftTargeted( self ) :
		# type: () -> bool
		pass
	def isAreaCleanPower( self ) :
		# type: () -> bool
		pass
	def isBarbarian( self ) :
		# type: () -> bool
		""" is owner a barbarian? """
	def isBombardable( self, arg0 ) :
		# type: (CyUnit) -> bool
		pass
	def isBombarded( self ) :
		# type: () -> bool
		pass
	def isBuildingOnlyHealthy( self ) :
		# type: () -> bool
		""" is the city ? """
	def isBuildingsMaxed( self ) :
		# type: () -> bool
		pass
	def isCapital( self ) :
		# type: () -> bool
		""" is city the owners capital? """
	def isCitizensAutomated( self ) :
		# type: () -> bool
		""" are citizens under automation? """
	def isCoastal( self, arg0 ) :
		# type: (int) -> bool
		""" is the city on the coast? """
	def isConnectedTo( self, arg0 ) :
		# type: (CyCity) -> bool
		""" is city connected to CyCity* via the Trade Network? """
	def isConnectedToCapital( self, iOwner ) :
		# type: (Any) -> bool
		""" connected to the capital? """
	def isDirtyPower( self ) :
		# type: () -> bool
		pass
	def isDisorder( self ) :
		# type: () -> bool
		""" is the city in disorder? """
	def isDrafted( self ) :
		# type: () -> bool
		pass
	def isEverOwned( self ) :
		# type: () -> bool
		pass
	def isFoodProduction( self ) :
		# type: () -> bool
		""" is item under construction being created with food instead of production? """
	def isFreePromotion( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isGovernmentCenter( self ) :
		# type: () -> bool
		""" is city the government center? """
	def isHasBuilding( self, arg0 ) :
		# type: (int) -> bool
		""" This function actually no longer exists in C++, this is a helper function which hooks up to getNumBuilding() to help mod backwards compatibility """
	def isHasCorporation( self, CorporationID ) :
		# type: (Any) -> bool
		""" does city have CorporationID? """
	def isHasReligion( self, ReligionID ) :
		# type: (Any) -> bool
		""" does city have ReligionID? """
	def isHeadquarters( self ) :
		# type: () -> bool
		""" is the city CorporationID's headquarters? """
	def isHeadquartersByType( self, CorporationID ) :
		# type: (Any) -> bool
		""" is the city CorporationID's headquarters? """
	def isHolyCity( self ) :
		# type: () -> bool
		""" is the city ReligionID's holy city? """
	def isHolyCityByType( self, ReligionID ) :
		# type: (Any) -> bool
		""" is the city ReligionID's holy city? """
	def isHuman( self ) :
		# type: () -> bool
		""" is owner human? """
	def isNationalWondersMaxed( self ) :
		# type: () -> bool
		pass
	def isNeverLost( self ) :
		# type: () -> bool
		pass
	def isNoBonus( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isNoUnhappiness( self ) :
		# type: () -> bool
		""" is the city unaffected by unhappiness? """
	def isNoUnhealthyPopulation( self ) :
		# type: () -> bool
		""" is the city unaffected by unhealthiness? """
	def isNone( self ) :
		# type: () -> None
		""" is the instance valid? """
	def isOccupation( self ) :
		# type: () -> bool
		""" is the city under occupation? """
	def isPlundered( self ) :
		# type: () -> bool
		pass
	def isPower( self ) :
		# type: () -> bool
		pass
	def isProduction( self ) :
		# type: () -> bool
		""" is city producing? """
	def isProductionAutomated( self ) :
		# type: () -> bool
		""" is production under automation? """
	def isProductionBuilding( self ) :
		# type: () -> bool
		""" is city constructing a building? """
	def isProductionLimited( self ) :
		# type: () -> bool
		pass
	def isProductionProcess( self ) :
		# type: () -> bool
		""" is city maintaining a process? """
	def isProductionProject( self ) :
		# type: () -> bool
		pass
	def isProductionUnit( self ) :
		# type: () -> bool
		""" is city training a unit? """
	def isRevealed( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def isSpecialistForced( self ) :
		# type: () -> bool
		pass
	def isSpecialistValid( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def isTeamWondersMaxed( self ) :
		# type: () -> bool
		pass
	def isTradeRoute( self ) :
		# type: () -> bool
		pass
	def isUnitFoodProduction( self, UnitID ) :
		# type: (Any) -> bool
		""" does UnitID require food to be trained? """
	def isVisible( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def isWallOverride( self ) :
		# type: () -> bool
		pass
	def isWorkingPlot( self, iIndex ) :
		# type: (Any) -> bool
		""" true if a worker is working this city's pPlot """
	def isWorkingPlotByIndex( self, iIndex ) :
		# type: (Any) -> bool
		""" true if a worker is working this city's plot iIndex """
	def isWorldWondersMaxed( self ) :
		# type: () -> bool
		pass
	def kill( self ) :
		# type: () -> None
		""" kill the city """
	def liberate( self ) :
		# type: () -> None
		pass
	def maxHurryPopulation( self ) :
		# type: () -> int
		pass
	def plot( self ) :
		# type: () -> CyPlot
		""" returns cities plot instance """
	def popOrder( self, arg0, arg1, arg2 ) :
		# type: (int, bool, bool) -> int
		pass
	def productionLeft( self ) :
		# type: () -> int
		""" result of (getProductionNeeded() - getProduction() """
	def pushOrder( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (int, int, int, bool, bool, bool, bool) -> None
		pass
	def setAirliftTargeted( self, iNewValue ) :
		# type: (Any) -> None
		pass
	def setBaseYieldRate( self, arg0, arg1 ) :
		# type: (int, int) -> int
		""" sets the base rate for YieldType """
	def setBombarded( self, iNewValue ) :
		# type: (Any) -> None
		pass
	def setBuildingCommerceChange( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def setBuildingHappyChange( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setBuildingHealthChange( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setBuildingProduction( self, BuildingID, iNewValue ) :
		# type: (Any, Any) -> None
		""" set progress towards BuildingID as iNewValue """
	def setBuildingProductionTime( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def setBuildingYieldChange( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def setCitizensAutomated( self, arg0 ) :
		# type: (bool) -> None
		""" set city animation bNewValue """
	def setCitySizeBoost( self, arg0 ) :
		# type: (int) -> Any
		pass
	def setCulture( self, *args, **kwargs ) :
		""" void (int PlayerTypes eIndex`, bool bPlots) """
	def setCultureTimes100( self, *args, **kwargs ) :
		""" void (int PlayerTypes eIndex, int iNewValue, bool bPlots) """
	def setDrafted( self, iNewValue ) :
		# type: (Any) -> None
		pass
	def setFeatureProduction( self, iNewValue ) :
		# type: (Any) -> None
		""" set feature production to iNewValue """
	def setFood( self, iNewValue ) :
		# type: (Any) -> None
		""" set stored food to iNewValue """
	def setForceSpecialistCount( self, *args, **kwargs ) :
		""" int (int /*SpecialistTypes*/ eIndex, int iNewValue """
	def setFreeSpecialistCount( self, *args, **kwargs ) :
		""" int (int /*SpecialistTypes*/ eIndex, iNewValue """
	def setGreatPeopleUnitProgress( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def setHasCorporation( self, CorporationID, arg1, arg2, arg3 ) :
		# type: (Any, bool, bool, bool) -> None
		""" corporation begins to spread """
	def setHasReligion( self, ReligionID, arg1, arg2, arg3 ) :
		# type: (Any, bool, bool, bool) -> None
		""" religion begins to spread """
	def setHighestPopulation( self, iNewValue ) :
		# type: (Any) -> None
		pass
	def setName( self, arg0, arg1 ) :
		# type: (TCHAR, bool) -> None
		""" sets the name to szNewValue """
	def setNeverLost( self, iNewValue ) :
		# type: (Any) -> None
		pass
	def setNumRealBuilding( self, BuildingID, iNum ) :
		# type: (Any, Any) -> Any
		""" Sets number of buildings in this city of BuildingID type """
	def setOccupationTimer( self, iNewValue ) :
		# type: (Any) -> None
		""" set the Occupation Timer to iNewValue """
	def setOverflowProduction( self, iNewValue ) :
		# type: (Any) -> None
		""" set overflow production to iNewValue """
	def setPlundered( self, iNewValue ) :
		# type: (Any) -> None
		pass
	def setPopulation( self, arg0 ) :
		# type: (int) -> None
		""" sets the city population to iNewValue """
	def setProduction( self, arg0 ) :
		# type: (int) -> None
		pass
	def setProductionAutomated( self, arg0 ) :
		# type: (bool) -> None
		""" set city production automation to bNewValue """
	def setRevealed( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def setScriptData( self, arg0 ) :
		# type: (str) -> None
		""" Set stored custom data (via pickle) """
	def setUnitProduction( self, UnitID, iNewValue ) :
		# type: (Any, Any) -> None
		""" sets production towards UnitID as iNewValue """
	def setWallOverride( self, arg0 ) :
		# type: (bool) -> Any
		pass
	def setWallOverridePoints( self, arg0 ) :
		# type: (Tuple) -> Any
		pass
	def totalBadBuildingHealth( self ) :
		# type: () -> int
		pass
	def totalFreeSpecialists( self, *args, **kwargs ) :
		pass
	def totalGoodBuildingHealth( self ) :
		# type: () -> int
		pass
	def totalTradeModifier( self ) :
		# type: () -> int
		""" total trade adjustment """
	def unhappyLevel( self, arg0 ) :
		# type: (int) -> int
		pass
	def unhealthyPopulation( self, *args, **kwargs ) :
		""" int (bool bNoAngry), int (iExtra) """
	def visiblePopulation( self ) :
		# type: () -> int
		pass
	def waterArea( self ) :
		# type: () -> CyArea
		pass

class CyDeal( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getFirstPlayer( self, *args, **kwargs ) :
		pass
	def getFirstTrade( self, *args, **kwargs ) :
		pass
	def getID( self, *args, **kwargs ) :
		pass
	def getInitialGameTurn( self, *args, **kwargs ) :
		pass
	def getLengthFirstTrades( self, *args, **kwargs ) :
		pass
	def getLengthSecondTrades( self, *args, **kwargs ) :
		pass
	def getSecondPlayer( self, *args, **kwargs ) :
		pass
	def getSecondTrade( self, *args, **kwargs ) :
		pass
	def isNone( self, *args, **kwargs ) :
		pass
	def kill( self, *args, **kwargs ) :
		pass

class CyDiplomacy( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def addUserComment( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, int, int, str, tuple) -> None
		pass
	def atWar( self ) :
		# type: () -> bool
		pass
	def clearUserComments( self ) :
		# type: () -> None
		pass
	def closeScreen( self ) :
		# type: () -> None
		pass
	def counterPropose( self ) :
		# type: () -> bool
		pass
	def declareWar( self ) :
		# type: () -> None
		pass
	def diploEvent( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def endTrade( self ) :
		# type: () -> None
		pass
	def getData( self ) :
		# type: () -> int
		pass
	def getOpponentCivName( self ) :
		# type: () -> unicode
		pass
	def getOpponentName( self ) :
		# type: () -> unicode
		pass
	def getOurCivName( self ) :
		# type: () -> unicode
		pass
	def getOurName( self ) :
		# type: () -> unicode
		pass
	def getOurScore( self ) :
		# type: () -> int
		pass
	def getPlayerTradeOffer( self, arg0 ) :
		# type: (int) -> TradeData
		pass
	def getTheirScore( self ) :
		# type: () -> int
		pass
	def getTheirTradeOffer( self, arg0 ) :
		# type: (int) -> TradeData
		pass
	def getWhoTradingWith( self, *args, **kwargs ) :
		""" int PlayerTypes*/ getWhoTradingWith() """
	def hasAnnualDeal( self ) :
		# type: () -> bool
		pass
	def implementDeal( self ) :
		# type: () -> None
		pass
	def isAIOffer( self ) :
		# type: () -> bool
		pass
	def isSeparateTeams( self ) :
		# type: () -> bool
		pass
	def makePeace( self ) :
		# type: () -> None
		pass
	def offerDeal( self ) :
		# type: () -> bool
		pass
	def ourOfferEmpty( self ) :
		# type: () -> bool
		pass
	def performHeadAction( self, arg0 ) :
		# type: (LeaderheadAction) -> None
		pass
	def setAIComment( self, arg0 ) :
		# type: (int) -> None
		pass
	def setAIOffer( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setAIString( self, arg0, arg1 ) :
		# type: (str, tuple) -> None
		pass
	def showAllTrade( self, arg0 ) :
		# type: (bool) -> None
		pass
	def startTrade( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def theirOfferEmpty( self ) :
		# type: () -> bool
		pass
	def theirVassalTribute( self ) :
		# type: () -> bool
		pass

class CyEngine( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def addColoredPlot( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, NiColorA, int) -> None
		pass
	def addColoredPlotAlt( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (int, int, int, int, str, float) -> None
		pass
	def addLandmark( self, arg0, arg1 ) :
		# type: (CyPlot, TCHAR) -> None
		pass
	def addLandmarkPopup( self, arg0 ) :
		# type: (CyPlot) -> None
		pass
	def addSign( self, arg0, arg1, arg2 ) :
		# type: (CyPlot, int, TCHAR) -> None
		pass
	def clearAreaBorderPlots( self, arg0 ) :
		# type: (int) -> None
		pass
	def clearColoredPlots( self, arg0 ) :
		# type: (int) -> None
		pass
	def fillAreaBorderPlot( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, NiColorA, int) -> None
		pass
	def fillAreaBorderPlotAlt( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, int, int, str, float) -> None
		pass
	def getCityBillboardVisibility( self ) :
		# type: () -> bool
		pass
	def getCultureVisibility( self ) :
		# type: () -> bool
		pass
	def getNumSigns( self ) :
		# type: () -> int
		pass
	def getSelectionCursorVisibility( self ) :
		# type: () -> bool
		pass
	def getSignByIndex( self, arg0 ) :
		# type: (int) -> CySign
		pass
	def getUnitFlagVisibility( self ) :
		# type: () -> bool
		pass
	def getUpdateRate( self ) :
		# type: () -> float
		pass
	def isDirty( self, arg0 ) :
		# type: (EngineDirtyBits) -> bool
		pass
	def isGlobeviewUp( self ) :
		# type: () -> bool
		pass
	def isNone( self ) :
		# type: () -> bool
		""" is the engine instance valid? """
	def reloadEffectInfos( self ) :
		# type: () -> None
		pass
	def removeLandmark( self, arg0 ) :
		# type: (CyPlot) -> None
		pass
	def removeSign( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> None
		pass
	def setCityBillboardVisibility( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setCultureVisibility( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setDirty( self, arg0, arg1 ) :
		# type: (EngineDirtyBits, bool) -> None
		pass
	def setFogOfWar( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setSelectionCursorVisibility( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setUnitFlagVisibility( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setUpdateRate( self, arg0 ) :
		# type: (float) -> None
		pass
	def toggleGlobeview( self ) :
		# type: () -> None
		pass
	def triggerEffect( self, iEffect, plotPoint ) :
		# type: (Any, Any) -> None
		pass

class CyFractal( object ) :
	class FracVals :
		DEFAULT_FRAC_X_EXP = 7 # type: CvPythonExtensions.FracVals
		DEFAULT_FRAC_Y_EXP = 6 # type: CvPythonExtensions.FracVals
		FRAC_CENTER_RIFT = 16 # type: CvPythonExtensions.FracVals
		FRAC_INVERT_HEIGHTS = 32 # type: CvPythonExtensions.FracVals
		FRAC_PERCENT = 4 # type: CvPythonExtensions.FracVals
		FRAC_POLAR = 8 # type: CvPythonExtensions.FracVals
		FRAC_WRAP_X = 1 # type: CvPythonExtensions.FracVals
		FRAC_WRAP_Y = 2 # type: CvPythonExtensions.FracVals
	def __init__( self, *args, **kwargs ) :
		pass
	def fracInit( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (int, int, int, CvRandom, int, int, int) -> None
		pass
	def fracInitHints( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (int, int, int, CvRandom, int, CyFractal, int, int) -> None
		pass
	def fracInitRifts( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (int, int, int, CvRandom, int, list, int, int) -> None
		pass
	def getHeight( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getHeightFromPercent( self, arg0 ) :
		# type: (int) -> int
		pass

class CyGFlyoutMenu( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def addTextItem( self, arg0, arg1, arg2 ) :
		# type: (unicode, str, str) -> None
		pass
	def create( self ) :
		# type: () -> None
		pass
	def destroy( self ) :
		# type: () -> None
		pass
	def hide( self ) :
		# type: () -> None
		pass
	def show( self ) :
		# type: () -> None
		pass

class CyGInterfaceScreen( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def addBonusGraphicGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12 ) :
		# type: (str, int, int, int, int, int, int, int, int, float, float, float, bool) -> None
		pass
	def addBuildingGraphicGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12 ) :
		# type: (str, int, int, int, int, int, int, int, int, float, float, float, bool) -> None
		pass
	def addCheckBoxGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, str, str, int, int, int, int, int, int, int, ButtonStyles) -> None
		pass
	def addCheckBoxGFCAt( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11 ) :
		# type: (str, str, str, int, int, int, int, int, int, int, ButtonStyles, bool) -> None
		pass
	def addDDSGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, str, int, int, int, int, int, int, int) -> None
		pass
	def addDDSGFCAt( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, str, str, int, int, int, int, int, int, int, bool) -> None
		pass
	def addDrawControl( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, str, int, int, int, int, int, int, int) -> None
		pass
	def addDrawControlAt( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, str, str, int, int, int, int, int, int, int) -> None
		pass
	def addDropDownBoxGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (str, int, int, int, int, int, int, int) -> None
		pass
	def addEditBoxGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, int, int, int, int, int, int, int, int) -> None
		pass
	def addFlagWidgetGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, int, int, int, int, int, int, int, int) -> None
		pass
	def addGraphData( self, arg0, arg1, arg2, arg3 ) :
		# type: (str, float, float, uint) -> None
		pass
	def addGraphLayer( self, arg0, arg1, arg2 ) :
		# type: (str, uint, int) -> None
		pass
	def addGraphWidget( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, str, str, float, float, float, float, float, int, int, int) -> None
		pass
	def addImprovementGraphicGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12 ) :
		# type: (str, int, int, int, int, int, int, int, int, float, float, float, bool) -> None
		pass
	def addItemToTableGFC( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (str, unicode, int, int, int) -> None
		pass
	def addLeaderheadGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, int, int, int, int, int, int, int, int, int) -> None
		pass
	def addLineGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, str, int, int, int, int, int) -> None
		pass
	def addListBoxGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, unicode, int, int, int, int, TableStyles) -> None
		pass
	def addModelGraphicGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11 ) :
		# type: (str, str, int, int, int, int, int, int, int, float, float, float) -> None
		pass
	def addMultiListControlGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, unicode, int, int, int, int, int, int, int, TableStyles) -> None
		pass
	def addMultiListControlGFCAt( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, unicode, int, int, int, int, int, int, int, TableStyles) -> None
		pass
	def addMultilineText( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, unicode, int, int, int, int, int, int, int, int) -> None
		pass
	def addPanel( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, unicode, unicode, bool, bool, int, int, int, int, PanelStyles) -> None
		pass
	def addPlotGraphicGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, int, int, int, int, CyPlot, int, bool, int, int, int) -> None
		pass
	def addPullDownString( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (str, unicode, int, int, bool) -> None
		pass
	def addReligionMovieWidgetGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, str, int, int, int, int, int, int, int) -> None
		pass
	def addScrollPanel( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, unicode, int, int, int, int, PanelStyles) -> None
		pass
	def addSimpleTableControlGFC( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, int, int, int, int, TableStyles) -> None
		pass
	def addSlider( self, *args, **kwargs ) :
		""" void ( string szName, int iX, int iY, int iWidth, int iHeight, int iDefault, int iMin, int iMax, WidgetTypes eWidgetType, int iData1, int iData2, bool bIsVertical=false ) """
	def addSpaceShipWidgetGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, int, int, int, int, int, int, int, int, int) -> None
		pass
	def addSpecificUnitGraphicGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12 ) :
		# type: (str, CyUnit, int, int, int, int, int, int, int, float, float, float, bool) -> None
		pass
	def addStackedBarGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, int, int, int, int, int, int, int, int) -> None
		pass
	def addStackedBarGFCAt( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, str, int, int, int, int, int, int, int, int) -> None
		pass
	def addTableControlGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, int, int, int, int, int, bool, bool, int, int, TableStyles) -> None
		pass
	def addTableControlGFCWithHelp( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11 ) :
		# type: (str, int, int, int, int, int, bool, bool, int, int, TableStyles, unicode) -> None
		pass
	def addTableHeaderGFC( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, unicode, int, int, int, int) -> None
		pass
	def addToModelGraphicGFC( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def addUnitGraphicGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12 ) :
		# type: (str, int, int, int, int, int, int, int, int, float, float, float, bool) -> None
		pass
	def appendListBoxString( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, unicode, int, int, int, int) -> None
		pass
	def appendListBoxStringNoUpdate( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, unicode, int, int, int, int) -> None
		pass
	def appendMultiListButton( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, str, int, int, int, int, bool) -> None
		pass
	def appendTableRow( self, arg0 ) :
		# type: (str) -> int
		pass
	def attachButtonGFC( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, str, unicode, int, int, int) -> None
		pass
	def attachCheckBoxGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, str, str, str, int, int, int, int, int, ButtonStyles) -> None
		pass
	def attachControlToTableCell( self, arg0, arg1, arg2, arg3 ) :
		# type: (str, str, int, int) -> None
		pass
	def attachDropDownBoxGFC( self, arg0, arg1, arg2 ) :
		# type: (str, str, bool) -> None
		pass
	def attachImageButton( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (str, str, str, GenericButtonSizes, int, int, int, bool) -> None
		pass
	def attachLabel( self, arg0, arg1, arg2 ) :
		# type: (str, str, unicode) -> None
		pass
	def attachListBoxGFC( self, arg0, arg1, arg2, arg3 ) :
		# type: (str, str, unicode, TableStyles) -> None
		pass
	def attachMultiListControlGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, str, unicode, int, int, int, TableStyles) -> None
		pass
	def attachMultilineText( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, str, unicode, int, int, int, int) -> None
		pass
	def attachPanel( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, str, unicode, unicode, bool, bool, PanelStyles) -> None
		pass
	def attachPanelAt( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13 ) :
		# type: (str, str, unicode, unicode, bool, bool, PanelStyles, int, int, int, int, int, int, int) -> None
		pass
	def attachSeparator( self, arg0, arg1, arg2 ) :
		# type: (str, str, bool) -> None
		pass
	def attachSlider( self, *args, **kwargs ) :
		""" void ( string szAttachTo, string szName, int iX, int iY, int iWidth, int iHeight, int iDefault, int iMin, int iMax, WidgetTypes eWidgetType, int iData1, int iData2, bool bIsVertical=false ) """
	def attachTableControlGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (str, str, int, bool, bool, int, int, TableStyles) -> None
		pass
	def attachTextGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, str, unicode, int, int, int, int) -> None
		pass
	def bringMinimapToFront( self, *args, **kwargs ) :
		""" void  """
	def centerX( self, arg0 ) :
		# type: (int) -> int
		pass
	def centerY( self, arg0 ) :
		# type: (int) -> int
		pass
	def changeDDSGFC( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def changeDrawControl( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def changeImageButton( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def changeModelGraphicTextureGFC( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def clearGraphData( self, arg0, arg1 ) :
		# type: (str, uint) -> None
		pass
	def clearListBoxGFC( self, arg0 ) :
		# type: (str) -> None
		pass
	def clearMultiList( self, arg0 ) :
		# type: (str) -> None
		pass
	def commitTableRow( self, arg0 ) :
		# type: (str) -> None
		pass
	def deleteWidget( self, arg0 ) :
		# type: (str) -> None
		pass
	def disableMultiListButton( self, arg0, arg1, arg2, arg3 ) :
		# type: (str, int, int, str) -> None
		pass
	def enable( self, arg0, arg1 ) :
		# type: (str, bool) -> None
		pass
	def enableGridlines( self, arg0, arg1, arg2 ) :
		# type: (str, bool, bool) -> None
		pass
	def enableMultiListPulse( self, arg0, arg1, arg2, arg3 ) :
		# type: (str, bool, int, int) -> None
		pass
	def enableSelect( self, arg0, arg1 ) :
		# type: (str, bool) -> None
		pass
	def enableSort( self, *args, **kwargs ) :
		pass
	def enableWorldSounds( self, arg0 ) :
		# type: (bool) -> None
		pass
	def getCheckBoxState( self, arg0 ) :
		# type: (str) -> bool
		pass
	def getCurrentTime( self ) :
		# type: () -> int
		pass
	def getEditBoxString( self, arg0 ) :
		# type: (str) -> unicode
		pass
	def getPullDownData( self, arg0, arg1 ) :
		# type: (str, int) -> int
		pass
	def getPullDownType( self, arg0, arg1 ) :
		# type: (str, int) -> int
		pass
	def getPythonFileID( self, *args, **kwargs ) :
		""" int  """
	def getRenderInterfaceOnly( self ) :
		# type: () -> bool
		pass
	def getScreenGroup( self ) :
		# type: () -> int
		pass
	def getSelectedPullDownID( self, arg0 ) :
		# type: (str) -> int
		pass
	def getTableNumColumns( self, arg0 ) :
		# type: (str) -> int
		pass
	def getTableNumRows( self, arg0 ) :
		# type: (str) -> int
		pass
	def getTableText( self, arg0, arg1, arg2 ) :
		# type: (str, int, int) -> None
		pass
	def getXResolution( self ) :
		# type: () -> int
		pass
	def getYResolution( self ) :
		# type: () -> int
		pass
	def hide( self, arg0 ) :
		# type: (str) -> None
		pass
	def hideEndTurn( self, arg0 ) :
		# type: (str) -> None
		pass
	def hideList( self, arg0 ) :
		# type: (int) -> None
		pass
	def hideScreen( self, *args, **kwargs ) :
		""" void  """
	def initMinimap( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, int, int, int, float) -> None
		pass
	def isActive( self ) :
		# type: () -> bool
		pass
	def isAlwaysShown( self ) :
		# type: () -> bool
		pass
	def isPersistent( self ) :
		# type: () -> bool
		pass
	def isRequiredForcedRedraw( self, *args, **kwargs ) :
		""" bool  """
	def isRowSelected( self, arg0, arg1 ) :
		# type: (str, int) -> bool
		pass
	def leaderheadKeyInput( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def markMinimapTexturePlotDirty( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def markRenderTexturesDirty( self ) :
		# type: () -> None
		pass
	def minimapClearAllFlashingTiles( self ) :
		# type: () -> None
		pass
	def minimapFlashPlot( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, int, float) -> None
		pass
	def modifyLabel( self, arg0, arg1, arg2 ) :
		# type: (str, unicode, int) -> None
		pass
	def modifyString( self, arg0, arg1, arg2 ) :
		# type: (str, unicode, int) -> None
		pass
	def moveBackward( self, arg0 ) :
		# type: (str) -> None
		pass
	def moveForward( self, arg0 ) :
		# type: (str) -> None
		pass
	def moveItem( self, arg0, arg1, arg2, arg3 ) :
		# type: (str, float, float, float) -> None
		pass
	def moveToBack( self, arg0 ) :
		# type: (str) -> None
		pass
	def moveToFront( self, arg0 ) :
		# type: (str) -> None
		pass
	def performLeaderheadAction( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def playMovie( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, float, float, float, float, float) -> None
		pass
	def prependListBoxString( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, unicode, int, int, int, int) -> None
		pass
	def registerHideList( self, arg0, arg1, arg2 ) :
		# type: (List, int, int) -> None
		pass
	def removeLineGFC( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def renderMinimapWorldTexture( self ) :
		# type: () -> None
		pass
	def selectMultiList( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def selectRow( self, arg0, arg1, arg2 ) :
		# type: (str, int, bool) -> None
		pass
	def setActivation( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def setAlwaysShown( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setBarPercentage( self, arg0, arg1, arg2 ) :
		# type: (str, int, float) -> None
		pass
	def setButtonGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, unicode, str, int, int, int, int, int, int, int, ButtonStyles) -> None
		pass
	def setCloseOnEscape( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setDimensions( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, int, int) -> None
		pass
	def setDying( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setEditBoxMaxCharCount( self, arg0, arg1, arg2 ) :
		# type: (str, int, int) -> None
		pass
	def setEditBoxString( self, arg0, arg1 ) :
		# type: (str, unicode) -> None
		pass
	def setEditBoxTextColor( self, arg0, arg1 ) :
		# type: (str, NiColorA) -> None
		pass
	def setEndTurnState( self, arg0, arg1 ) :
		# type: (str, unicode) -> None
		pass
	def setExitText( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (unicode, int, float, float, float, int) -> None
		pass
	def setFocus( self, arg0 ) :
		# type: (str) -> None
		pass
	def setForcedRedraw( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setGraphGrid( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (str, float, float, float, float) -> None
		pass
	def setGraphLabelX( self, arg0, arg1 ) :
		# type: (str, unicode) -> None
		pass
	def setGraphLabelY( self, arg0, arg1 ) :
		# type: (str, unicode) -> None
		pass
	def setGraphXDataRange( self, arg0, arg1, arg2 ) :
		# type: (str, float, float) -> None
		pass
	def setGraphYDataRange( self, arg0, arg1, arg2 ) :
		# type: (str, float, float) -> None
		pass
	def setHelpLabel( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, str, unicode, int, float, float, float, int, unicode) -> None
		pass
	def setHelpTextArea( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (float, int, float, float, float, bool, str, bool, bool, uint, int) -> None
		pass
	def setHelpTextString( self, arg0 ) :
		# type: (unicode) -> None
		pass
	def setHitTest( self, arg0, arg1 ) :
		# type: (str, hitTestTypes) -> None
		pass
	def setImageButton( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, str, int, int, int, int, int, int, int) -> None
		pass
	def setImageButtonAt( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, str, str, int, int, int, int, int, int, int) -> None
		pass
	def setLabel( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, str, unicode, int, float, float, float, int, int, int, int) -> None
		pass
	def setLabelAt( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, str, unicode, int, float, float, float, int, int, int, int) -> None
		pass
	def setLeaderheadAdvisor( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def setLeaderheadMood( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def setListBoxStringGFC( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, int, unicode, int, int, int, int) -> None
		pass
	def setMainInterface( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setMinimapColor( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, int, int, int, float) -> None
		pass
	def setMinimapMap( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (CyReplayInfo, int, int, int, int, float) -> None
		pass
	def setMinimapMode( self, arg0 ) :
		# type: (int) -> None
		pass
	def setMinimapNoRender( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setMinimapSectionOverride( self, arg0, arg1, arg2, arg3 ) :
		# type: (float, float, float, float) -> None
		pass
	def setModelGraphicRotationRateGFC( self, arg0, arg1 ) :
		# type: (str, float) -> None
		pass
	def setPanelColor( self, arg0, arg1, arg2, arg3 ) :
		# type: (str, int, int, int) -> None
		pass
	def setPanelSize( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (str, int, int, int, int) -> None
		pass
	def setPersistent( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setRenderInterfaceOnly( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setScreenGroup( self, arg0 ) :
		# type: (int) -> None
		pass
	def setSelectedListBoxStringGFC( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def setShowFor( self, *args, **kwargs ) :
		pass
	def setSound( self, arg0 ) :
		# type: (str) -> None
		pass
	def setSoundId( self, arg0 ) :
		# type: (int) -> None
		pass
	def setSpaceShip( self, arg0 ) :
		# type: (int) -> None
		pass
	def setStackedBarColors( self, arg0, arg1, arg2 ) :
		# type: (str, int, int) -> None
		pass
	def setStackedBarColorsAlpha( self, arg0, arg1, arg2, arg3 ) :
		# type: (str, int, int, float) -> None
		pass
	def setStackedBarColorsRGB( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, int, int, int, int, float) -> None
		pass
	def setState( self, arg0, arg1 ) :
		# type: (str, bool) -> None
		pass
	def setStyle( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def setTableColumnHeader( self, arg0, arg1, arg2, arg3 ) :
		# type: (str, int, unicode, int) -> None
		pass
	def setTableColumnRightJustify( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def setTableDate( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, int, int, unicode, str, int, int, int, int) -> None
		pass
	def setTableInt( self, *args, **kwargs ) :
		pass
	def setTableNumRows( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def setTableRowHeight( self, arg0, arg1, arg2 ) :
		# type: (str, int, int) -> None
		pass
	def setTableText( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, int, int, unicode, str, int, int, int, int) -> None
		pass
	def setTableTextKey( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9 ) :
		# type: (str, int, unicode, int, unicode, int, int, int, int, int) -> None
		pass
	def setText( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, str, unicode, int, float, float, float, int, int, int, int) -> None
		pass
	def setTextAt( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, str, unicode, int, float, float, float, int, int, int, int) -> None
		pass
	def setToolTipAlignment( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def setViewMin( self, arg0, arg1, arg2 ) :
		# type: (str, int, int) -> None
		pass
	def show( self, arg0 ) :
		# type: (str) -> None
		pass
	def showEndTurn( self, arg0 ) :
		# type: (str) -> None
		pass
	def showScreen( self, arg0, arg1 ) :
		# type: (PopupStates, bool) -> None
		pass
	def showWindowBackground( self, arg0 ) :
		# type: (bool) -> None
		pass
	def spaceShipCanChangeType( self, arg0 ) :
		# type: (int) -> bool
		pass
	def spaceShipChangeType( self, arg0 ) :
		# type: (int) -> None
		pass
	def spaceShipFinalize( self ) :
		# type: () -> None
		pass
	def spaceShipLaunch( self ) :
		# type: () -> None
		pass
	def spaceShipZoom( self, arg0 ) :
		# type: (int) -> None
		pass
	def updateAppropriateCitySelection( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def updateListBox( self, arg0 ) :
		# type: (str) -> None
		pass
	def updateMinimap( self, arg0 ) :
		# type: (float) -> None
		pass
	def updateMinimapColorFromMap( self, arg0, arg1 ) :
		# type: (int, float) -> None
		pass
	def updateMinimapSection( self, arg0 ) :
		# type: (bool) -> None
		pass
	def updateMinimapVisibility( self, *args, **kwargs ) :
		""" void  """

class CyGTabCtrl( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def addSectionButton( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (char, str, str, str, int) -> None
		pass
	def addSectionCheckbox( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (char, str, str, str, int, bool) -> None
		pass
	def addSectionDropdown( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (List[str], str, str, str, int, int) -> None
		pass
	def addSectionEditCtrl( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (char, str, str, str, int) -> None
		pass
	def addSectionLabel( self, arg0, arg1 ) :
		# type: (char, int) -> None
		pass
	def addSectionRadioButton( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (char, str, str, str, int, bool) -> None
		pass
	def addSectionSeparator( self, iTab ) :
		# type: (Any) -> None
		pass
	def addSectionSlider( self, *args, **kwargs ) :
		""" std::wstring szLabel, const std::string& szPythonCBModule, const std::string& szPythonCBFxn, const std::string& szPythonID, int iTabIndex, int iMin, int iMax, int iInitialVal, int iFormatNumber, int iFormatDecimal """
	def addSectionSpinner( self, *args, **kwargs ) :
		""" std::wstring szLabel, const std::string& szPythonCBModule, const std::string& szPythonCBFxn, const std::string& szPythonID, int iTabIndex, float fMin, float fMax, float fInc, float fInitialVal) """
	def addTabSection( self, arg0 ) :
		# type: (char) -> None
		pass
	def attachButton( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, str, unicode, str, str, str) -> None
		pass
	def attachCheckBox( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, str, unicode, str, str, str, bool) -> None
		pass
	def attachDropDown( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (str, str, char, Tuple, str, str, str, int) -> None
		pass
	def attachEdit( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, str, unicode, str, str, str) -> None
		pass
	def attachExpandSpacer( self, arg0 ) :
		# type: (str) -> None
		pass
	def attachFixedSpacer( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def attachHBox( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def attachHSeparator( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def attachHSlider( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (str, str, str, str, str, int, int, int) -> None
		pass
	def attachImage( self, arg0, arg1, arg2 ) :
		# type: (str, str, unicode) -> None
		pass
	def attachLabel( self, arg0, arg1, arg2 ) :
		# type: (str, str, unicode) -> None
		pass
	def attachPanel( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def attachRadioButton( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, str, unicode, str, str, str, bool) -> None
		pass
	def attachScrollPanel( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def attachSpacer( self, arg0 ) :
		# type: (str) -> None
		pass
	def attachSpinner( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (str, str, str, str, str, float, float, float, float, int, int) -> None
		pass
	def attachTabItem( self, arg0, arg1 ) :
		# type: (str, unicode) -> None
		pass
	def attachTitledPanel( self, arg0, arg1, arg2 ) :
		# type: (str, str, unicode) -> None
		pass
	def attachVBox( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def attachVSeparator( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def attachVSlider( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (str, str, str, str, str, int, int, int) -> None
		pass
	def changeDropdownContents( self, arg0, arg1 ) :
		# type: (str, tuple) -> None
		pass
	def create( self ) :
		# type: () -> None
		pass
	def createByName( self, arg0 ) :
		# type: (char) -> None
		pass
	def destroy( self ) :
		# type: () -> None
		pass
	def enable( self, arg0 ) :
		# type: (bool) -> None
		pass
	def getActiveTab( self ) :
		# type: () -> bool
		pass
	def getCheckBoxState( self, arg0, arg1 ) :
		# type: (char, wchar) -> None
		pass
	def getControlsExpanding( self, *args, **kwargs ) :
		""" bool getControlsExpanding() const """
	def getDropDownSelection( self, arg0, arg1 ) :
		# type: (char, char) -> None
		pass
	def getRadioButtonState( self, arg0, arg1 ) :
		# type: (char, wchar) -> None
		pass
	def getRadioValue( self, arg0 ) :
		# type: (str) -> float
		pass
	def getText( self, arg0 ) :
		# type: (str) -> unicode
		pass
	def getValue( self, arg0 ) :
		# type: (str) -> float
		pass
	def isEnabled( self ) :
		# type: () -> bool
		pass
	def isNone( self ) :
		# type: () -> bool
		""" Is this instance valid? """
	def setActivation( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def setActiveTab( self, arg0 ) :
		# type: (int) -> None
		pass
	def setCheckBoxState( self, arg0, arg1, arg2 ) :
		# type: (char, wchar, bool) -> None
		pass
	def setColumnLength( self, arg0 ) :
		# type: (int) -> None
		pass
	def setControlFlag( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def setControlsExpanding( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setDropDownSelection( self, arg0, arg1, arg2 ) :
		# type: (char, char, int) -> None
		pass
	def setEditCtrlText( self, arg0, arg1, arg2 ) :
		# type: (unicode, unicode, unicode) -> None
		pass
	def setEnabled( self, arg0, arg1 ) :
		# type: (str, bool) -> None
		pass
	def setFocus( self, arg0 ) :
		# type: (str) -> None
		pass
	def setHitTest( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def setKeyFocus( self, arg0, arg1, arg2 ) :
		# type: (str, str, str) -> None
		pass
	def setLayoutFlag( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def setModal( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setNumColumns( self, arg0 ) :
		# type: (int) -> None
		pass
	def setRadioButtonState( self, *args, **kwargs ) :
		""" void setRadiioButtonState(const char *szTabName, const wchar *szButtonText, bool bState) """
	def setRadioValue( self, arg0, arg1 ) :
		# type: (str, float) -> None
		pass
	def setSize( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setSliderWidth( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def setStyle( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def setTabFocus( self, arg0, arg1, arg2 ) :
		# type: (str, str, str) -> None
		pass
	def setText( self, arg0, arg1 ) :
		# type: (str, unicode) -> None
		pass
	def setToolTip( self, arg0, arg1 ) :
		# type: (str, unicode) -> None
		pass
	def setValue( self, arg0, arg1 ) :
		# type: (str, float) -> None
		pass
	def toggle( self ) :
		# type: () -> None
		pass

class CyGame( object ) :
	def GetWorldBuilderMode( self, *args, **kwargs ) :
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	def addDeal( self, *args, **kwargs ) :
		pass
	def addPlayer( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def calculateOptionsChecksum( self, *args, **kwargs ) :
		pass
	def calculateReligionPercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def calculateSyncChecksum( self, *args, **kwargs ) :
		pass
	def canHaveSecretaryGeneral( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canTrainNukes( self ) :
		# type: () -> bool
		pass
	def changeDiploVote( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeFreeTradeCount( self, *args, **kwargs ) :
		pass
	def changeMaxTurns( self, *args, **kwargs ) :
		pass
	def changeNoNukesCount( self, *args, **kwargs ) :
		pass
	def changeNukesExploded( self, *args, **kwargs ) :
		pass
	def changePlotExtraCost( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def changeTradeRoutes( self, *args, **kwargs ) :
		pass
	def cityPushOrder( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (CyCity, int, int, bool, bool, bool) -> None
		pass
	def clearHeadquarters( self, arg0 ) :
		# type: (int) -> None
		""" clears the headquarters for corporation eIndex """
	def clearHolyCity( self, arg0 ) :
		# type: (int) -> None
		""" clears the holy city for religion eIndex """
	def countCivPlayersAlive( self ) :
		# type: () -> int
		pass
	def countCivPlayersEverAlive( self ) :
		# type: () -> int
		pass
	def countCivTeamsAlive( self ) :
		# type: () -> int
		pass
	def countCivTeamsEverAlive( self ) :
		# type: () -> int
		pass
	def countCorporationLevels( self, arg0 ) :
		# type: (int) -> int
		pass
	def countHumanPlayersAlive( self ) :
		# type: () -> int
		pass
	def countKnownTechNumTeams( self, arg0 ) :
		# type: (int) -> int
		pass
	def countNumHumanGameTurnActive( self, *args, **kwargs ) :
		pass
	def countPossibleVote( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def countReligionLevels( self, arg0 ) :
		# type: (int) -> int
		pass
	def countTotalCivPower( self ) :
		# type: () -> int
		pass
	def countTotalNukeUnits( self ) :
		# type: () -> int
		pass
	def cycleCities( self, arg0, arg1 ) :
		# type: (bool, bool) -> None
		pass
	def cyclePlotUnits( self, arg0, arg1, arg2, arg3 ) :
		# type: (CyPlot, bool, bool, int) -> bool
		pass
	def cycleSelectionGroups( self, arg0, arg1, arg2 ) :
		# type: (bool, bool, bool) -> None
		pass
	def doControl( self, arg0 ) :
		# type: (int) -> None
		pass
	def getAIAutoPlay( self, *args, **kwargs ) :
		pass
	def getActiveCivilizationType( self ) :
		# type: () -> int
		""" returns CivilizationID """
	def getActivePlayer( self, *args, **kwargs ) :
		""" returns index of the active player """
	def getActiveTeam( self ) :
		# type: () -> int
		""" returns ID for the group """
	def getAdjustedLandPercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getAdjustedPopulationPercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBestLandUnit( self, *args, **kwargs ) :
		""" returns index of the best unit """
	def getBestLandUnitCombat( self ) :
		# type: () -> int
		pass
	def getBuildingClassCreatedCount( self, BuildingClassType ) :
		# type: (Any) -> int
		""" building Class count """
	def getCalendar( self ) :
		# type: () -> CalendarType
		pass
	def getCorporationGameTurnFounded( self, *args, **kwargs ) :
		pass
	def getCultureThreshold( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCurrentEra( self ) :
		# type: () -> int
		pass
	def getCurrentLanguage( self, *args, **kwargs ) :
		pass
	def getDeal( self, *args, **kwargs ) :
		pass
	def getElapsedGameTurns( self ) :
		# type: () -> int
		""" Elapsed turns thus far """
	def getEstimateEndTurn( self, *args, **kwargs ) :
		pass
	def getForceCivicCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFreeTradeCount( self, *args, **kwargs ) :
		pass
	def getGameSpeedType( self, *args, **kwargs ) :
		pass
	def getGameState( self, *args, **kwargs ) :
		pass
	def getGameTurn( self ) :
		# type: () -> int
		""" current game turn """
	def getGameTurnYear( self, *args, **kwargs ) :
		pass
	def getHandicapType( self ) :
		# type: () -> HandicapType
		""" difficulty level settings """
	def getHeadquarters( self ) :
		# type: () -> CyCity
		pass
	def getHolyCity( self ) :
		# type: () -> CyCity
		pass
	def getImprovementUpgradeTime( self, arg0 ) :
		# type: (int) -> int
		pass
	def getIndexAfterLastDeal( self, *args, **kwargs ) :
		pass
	def getInitLand( self, *args, **kwargs ) :
		pass
	def getInitPopulation( self, *args, **kwargs ) :
		pass
	def getInitTech( self, *args, **kwargs ) :
		pass
	def getInitWonders( self, *args, **kwargs ) :
		pass
	def getMapRand( self, *args, **kwargs ) :
		pass
	def getMapRandNum( self, *args, **kwargs ) :
		pass
	def getMaxCityElimination( self, *args, **kwargs ) :
		pass
	def getMaxLand( self, *args, **kwargs ) :
		pass
	def getMaxPopulation( self, *args, **kwargs ) :
		pass
	def getMaxTech( self, *args, **kwargs ) :
		pass
	def getMaxTurns( self, *args, **kwargs ) :
		pass
	def getMaxWonders( self, *args, **kwargs ) :
		pass
	def getMinutesPlayed( self, *args, **kwargs ) :
		""" Returns the number of minutes since the game began """
	def getName( self, *args, **kwargs ) :
		pass
	def getNoNukesCount( self, *args, **kwargs ) :
		pass
	def getNukesExploded( self, *args, **kwargs ) :
		pass
	def getNumAdvancedStartPoints( self, *args, **kwargs ) :
		pass
	def getNumCities( self ) :
		# type: () -> int
		""" total cities in Game """
	def getNumCivCities( self ) :
		# type: () -> int
		""" total non-barbarian cities in Game """
	def getNumDeals( self, *args, **kwargs ) :
		pass
	def getNumFreeBonuses( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNumGameTurnActive( self, *args, **kwargs ) :
		pass
	def getNumHumanPlayers( self ) :
		# type: () -> int
		""" # of human players in-game """
	def getNumReplayMessages( self, *args, **kwargs ) :
		pass
	def getPausePlayer( self ) :
		# type: () -> int
		""" will get who paused us """
	def getPitbossTurnTime( self ) :
		# type: () -> int
		pass
	def getPlayerRank( self, *args, **kwargs ) :
		pass
	def getPlayerScore( self, *args, **kwargs ) :
		pass
	def getPlayerVote( self, *args, **kwargs ) :
		pass
	def getProductionPerPopulation( self, arg0 ) :
		# type: (int) -> int
		pass
	def getProjectCreatedCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getRankPlayer( self, *args, **kwargs ) :
		pass
	def getRankTeam( self, *args, **kwargs ) :
		pass
	def getReligionGameTurnFounded( self, *args, **kwargs ) :
		pass
	def getReplayInfo( self, *args, **kwargs ) :
		pass
	def getReplayMessageColor( self, *args, **kwargs ) :
		pass
	def getReplayMessagePlayer( self, *args, **kwargs ) :
		pass
	def getReplayMessagePlotX( self, *args, **kwargs ) :
		pass
	def getReplayMessagePlotY( self, *args, **kwargs ) :
		pass
	def getReplayMessageText( self, *args, **kwargs ) :
		pass
	def getReplayMessageTurn( self, *args, **kwargs ) :
		pass
	def getReplayMessageType( self, *args, **kwargs ) :
		pass
	def getScriptData( self ) :
		# type: () -> str
		""" Returns ScriptData member (used to store custom data) """
	def getSecretaryGeneral( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSecretaryGeneralTimer( self, *args, **kwargs ) :
		pass
	def getSorenRand( self, *args, **kwargs ) :
		pass
	def getSorenRandNum( self, *args, **kwargs ) :
		pass
	def getStartEra( self, *args, **kwargs ) :
		pass
	def getStartTurn( self ) :
		# type: () -> int
		""" Returns the starting Turn (0 unless a scenario or advanced era start) """
	def getStartYear( self ) :
		# type: () -> int
		""" Returns the starting year (e.g. -4000) """
	def getSymbolID( self, arg0 ) :
		# type: (int) -> int
		pass
	def getTargetScore( self, *args, **kwargs ) :
		pass
	def getTeamRank( self, *args, **kwargs ) :
		pass
	def getTeamScore( self, *args, **kwargs ) :
		pass
	def getTotalPopulation( self ) :
		# type: () -> int
		""" total game population """
	def getTradeRoutes( self, *args, **kwargs ) :
		pass
	def getTurnSlice( self, *args, **kwargs ) :
		pass
	def getTurnYear( self, iGameTurn ) :
		# type: (Any) -> int
		""" turn Time """
	def getUnitClassCreatedCount( self, eIndex ) :
		# type: (Any) -> int
		""" returns number of this unit class type created (?) """
	def getUnitCreatedCount( self, eIndex ) :
		# type: (Any) -> int
		""" returns number of this unit type created (?) """
	def getVictory( self, *args, **kwargs ) :
		pass
	def getVoteOutcome( self, arg0 ) :
		# type: (int) -> int
		pass
	def getVoteRequired( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getVoteSourceReligion( self, arg0 ) :
		# type: (int) -> int
		pass
	def getVoteTimer( self, *args, **kwargs ) :
		pass
	def getWinner( self, *args, **kwargs ) :
		pass
	def goldenAgeLength( self ) :
		# type: () -> int
		pass
	def hasSkippedSaveChecksum( self, *args, **kwargs ) :
		pass
	def isBuildingClassMaxedOut( self, BuildingClassType ) :
		# type: (Any) -> bool
		""" max # reached? """
	def isBuildingEverActive( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isChooseElection( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isCircumnavigated( self ) :
		# type: () -> bool
		""" is the globe circumnavigated? """
	def isCivEverActive( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isCorporationFounded( self, CorporationID ) :
		# type: (Any) -> bool
		""" is corporation founded? """
	def isDebugMode( self ) :
		# type: () -> bool
		""" is the game in Debug Mode? """
	def isDiploVote( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isEventActive( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isFinalInitialized( self ) :
		# type: () -> bool
		""" Returns whether or not the game initialization process has ended (game has started) """
	def isForceCivic( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isForceCivicOption( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isForcedControl( self, eIndex ) :
		# type: (Any) -> bool
		""" returns whether Control should be forced """
	def isFreeTrade( self, *args, **kwargs ) :
		pass
	def isGameMultiPlayer( self ) :
		# type: () -> bool
		""" GameMultiplayer()? """
	def isHotSeat( self ) :
		# type: () -> bool
		pass
	def isInAdvancedStart( self, *args, **kwargs ) :
		""" bool """
	def isLeaderEverActive( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isMPOption( self, eIndex ) :
		# type: (Any) -> bool
		""" returns whether MP Option is valid """
	def isModem( self ) :
		# type: () -> bool
		""" Using a modem? """
	def isNetworkMultiPlayer( self ) :
		# type: () -> bool
		""" NetworkMultiplayer()? """
	def isNoNukes( self, *args, **kwargs ) :
		pass
	def isNone( self ) :
		# type: () -> CyGame
		""" is the instance valid? """
	def isNukesValid( self, *args, **kwargs ) :
		""" bool """
	def isOption( self, eIndex ) :
		# type: (Any) -> bool
		""" returns whether Game Option is valid """
	def isPaused( self ) :
		# type: () -> bool
		""" will say if the game is paused """
	def isPbem( self ) :
		# type: () -> bool
		pass
	def isPitboss( self ) :
		# type: () -> bool
		pass
	def isPitbossHost( self, *args, **kwargs ) :
		pass
	def isProjectMaxedOut( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isReligionFounded( self, ReligionID ) :
		# type: (Any) -> bool
		""" is religion founded? """
	def isReligionSlotTaken( self, ReligionID ) :
		# type: (Any) -> bool
		""" is religion in that tech slot founded? """
	def isScoreDirty( self ) :
		# type: () -> bool
		pass
	def isSimultaneousTeamTurns( self ) :
		# type: () -> bool
		pass
	def isSpecialBuildingValid( self, *args, **kwargs ) :
		pass
	def isSpecialUnitValid( self, *args, **kwargs ) :
		pass
	def isTeamGame( self ) :
		# type: () -> bool
		pass
	def isTeamVote( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isTeamVoteEligible( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def isUnitClassMaxedOut( self, eIndex, iExtra ) :
		# type: (Any, Any) -> bool
		""" returns whether or not this unit class is maxed out (e.g. spies) """
	def isUnitEverActive( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isVictoryValid( self, *args, **kwargs ) :
		pass
	def isVotePassed( self, *args, **kwargs ) :
		pass
	def makeCircumnavigated( self, *args, **kwargs ) :
		pass
	def makeNukesValid( self, arg0 ) :
		# type: (bool) -> None
		pass
	def makeSpecialBuildingValid( self, *args, **kwargs ) :
		pass
	def makeSpecialUnitValid( self, *args, **kwargs ) :
		pass
	def reviveActivePlayer( self ) :
		# type: () -> None
		pass
	def saveReplay( self, *args, **kwargs ) :
		pass
	def selectedCitiesGameNetMessage( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (int, int, int, int, bool, bool, bool, bool) -> None
		pass
	def selectionListGameNetMessage( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (int, int, int, int, int, bool, bool) -> None
		pass
	def selectionListMove( self, arg0, arg1, arg2, arg3 ) :
		# type: (CyPlot, bool, bool, bool) -> None
		pass
	def setAIAutoPlay( self, *args, **kwargs ) :
		pass
	def setActivePlayer( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def setCurrentLanguage( self, *args, **kwargs ) :
		pass
	def setEstimateEndTurn( self, *args, **kwargs ) :
		pass
	def setGameTurn( self, iNewValue ) :
		# type: (Any) -> None
		""" set current game turn """
	def setHeadquarters( self, arg0, arg1, bAnnounce ) :
		# type: (int, CyCity, Any) -> None
		""" Sets headquarters for corporation eIndex to pNewValue """
	def setHolyCity( self, arg0, arg1, bAnnounce ) :
		# type: (int, CyCity, Any) -> None
		""" Sets holy city for religion eIndex to pNewValue """
	def setMaxCityElimination( self, *args, **kwargs ) :
		pass
	def setMaxTurns( self, *args, **kwargs ) :
		pass
	def setModem( self, arg0 ) :
		# type: (bool) -> None
		""" Use a modem! (or don't) """
	def setName( self, *args, **kwargs ) :
		pass
	def setNumAdvancedStartPoints( self, *args, **kwargs ) :
		pass
	def setOption( self, GameOptionIndex, bEnabled ) :
		# type: (Any, Any) -> None
		""" sets a Game Option """
	def setPitbossTurnTime( self, arg0 ) :
		# type: (int) -> None
		pass
	def setPlotExtraYield( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, int, int) -> None
		pass
	def setScoreDirty( self, *args, **kwargs ) :
		pass
	def setScriptData( self, arg0 ) :
		# type: (str) -> None
		""" Sets ScriptData member (used to store custom data) """
	def setStartYear( self ) :
		# type: () -> None
		""" Sets the starting year (e.g. -4000) """
	def setTargetScore( self, *args, **kwargs ) :
		pass
	def setVoteSourceReligion( self, arg0, arg1, arg2 ) :
		# type: (int, int, bool) -> None
		pass
	def setWinner( self, *args, **kwargs ) :
		pass
	def toggleDebugMode( self, *args, **kwargs ) :
		pass
	def updateScore( self, arg0 ) :
		# type: (bool) -> None
		pass
	def victoryDelay( self, arg0 ) :
		# type: (int) -> int
		pass

class CyGameTextMgr( object ) :
	def Reset( self ) :
		# type: () -> None
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	def buildHintsList( self ) :
		# type: () -> unicode
		pass
	def getActiveDealsString( self, arg0, arg1 ) :
		# type: (int, int) -> unicode
		pass
	def getAttitudeString( self, arg0, arg1 ) :
		# type: (int, int) -> unicode
		pass
	def getBonusHelp( self, arg0, arg1 ) :
		# type: (int, bool) -> unicode
		pass
	def getBuildingHelp( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, bool, bool, bool, CyCity) -> unicode
		pass
	def getCorporationHelpCity( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, CyCity, bool, bool) -> unicode
		pass
	def getDateStr( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, bool, int, int, int) -> unicode
		pass
	def getDealString( self, arg0, arg1 ) :
		# type: (CyDeal, int) -> unicode
		pass
	def getFeatureHelp( self, arg0, arg1 ) :
		# type: (int, bool) -> unicode
		pass
	def getGoldStr( self, arg0 ) :
		# type: (int) -> unicode
		pass
	def getImprovementHelp( self, arg0, arg1 ) :
		# type: (int, bool) -> unicode
		pass
	def getInterfaceTimeStr( self, arg0 ) :
		# type: (int) -> unicode
		pass
	def getNetStats( self, arg0 ) :
		# type: (int) -> unicode
		pass
	def getOOSSeeds( self, arg0 ) :
		# type: (int) -> unicode
		pass
	def getProjectHelp( self, arg0, arg1, arg2 ) :
		# type: (int, bool, CyCity) -> unicode
		pass
	def getPromotionHelp( self, arg0, arg1 ) :
		# type: (int, bool) -> unicode
		pass
	def getReligionHelpCity( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, CyCity, bool, bool, bool) -> unicode
		pass
	def getResearchStr( self, arg0 ) :
		# type: (int) -> unicode
		pass
	def getSpecialistHelp( self, arg0, arg1, arg2 ) :
		# type: (TradeData, int, int) -> unicode
		pass
	def getSpecificUnitHelp( self, arg0, arg1, arg2 ) :
		# type: (CyUnit, bool, bool) -> unicode
		pass
	def getTechHelp( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (int, bool, bool, bool, bool, int) -> unicode
		pass
	def getTerrainHelp( self, arg0, arg1 ) :
		# type: (int, bool) -> unicode
		pass
	def getTimeStr( self, arg0, arg1 ) :
		# type: (int, bool) -> unicode
		pass
	def getTradeString( self, arg0, arg1 ) :
		# type: (int, bool) -> unicode
		pass
	def getUnitHelp( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, bool, bool, bool, CyCity) -> unicode
		pass
	def isNone( self ) :
		# type: () -> bool
		""" Checks to see if pointer points to a real object """
	def parseCivInfos( self, arg0, arg1 ) :
		# type: (int, bool) -> unicode
		pass
	def parseCivicInfo( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, bool, bool, bool) -> unicode
		pass
	def parseCorporationInfo( self, arg0, arg1 ) :
		# type: (int, bool) -> unicode
		pass
	def parseLeaderTraits( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, bool, bool) -> unicode
		pass
	def parseReligionInfo( self, arg0, arg1 ) :
		# type: (int, bool) -> unicode
		pass
	def setConvertHelp( self, arg0, arg1 ) :
		# type: (int, int) -> unicode
		pass
	def setRevolutionHelp( self, arg0 ) :
		# type: (int) -> unicode
		pass
	def setVassalRevoltHelp( self, arg0, arg1 ) :
		# type: (int, int) -> unicode
		pass

class CyGlobalContext( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getAIR_BOMB_HEIGHT( self ) :
		# type: () -> float
		pass
	def getAMPHIB_ATTACK_MODIFIER( self ) :
		# type: () -> int
		pass
	def getASyncRand( self, *args, **kwargs ) :
		""" Non-Synch'd random # """
	def getActionInfo( self, arg0 ) :
		# type: (int) -> CvActionInfo
		""" CvInfo for ActionID """
	def getActivePlayer( self ) :
		# type: () -> Any
		""" active player instance """
	def getAnimationOperatorTypes( self ) :
		# type: () -> str
		""" Returns enum string """
	def getArtStyleTypes( self ) :
		# type: () -> str
		""" Returns enum string """
	def getAttitudeInfo( self, arg0 ) :
		# type: (int) -> CvAttitudeInfo
		pass
	def getAutomateInfo( self, arg0 ) :
		# type: (int) -> CvAutomateInfo
		""" CvInfo for AutomateID """
	def getBARBARIAN_PLAYER( self ) :
		# type: () -> int
		pass
	def getBARBARIAN_TEAM( self ) :
		# type: () -> int
		pass
	def getBonusArtInfo( self, arg0 ) :
		# type: (int) -> CvBonusArtInfo
		""" Returns info object """
	def getBonusClassInfo( self, arg0 ) :
		# type: (int) -> CvBonusClassInfo
		""" CvInfo for BonusID """
	def getBonusInfo( self, arg0 ) :
		# type: (int) -> CvBonusInfo
		""" CvInfo for BonusID """
	def getBuildInfo( self, arg0 ) :
		# type: (int) -> CvBuildInfo
		""" CvInfo for BuildID """
	def getBuildingArtInfo( self, arg0 ) :
		# type: (int) -> CvBuildingArtInfo
		""" CvArtInfo for BuildingID """
	def getBuildingClassInfo( self, arg0 ) :
		# type: (int) -> CvBuildingClassInfo
		""" CvInfo for BuildingClassID """
	def getBuildingInfo( self, arg0 ) :
		# type: (int) -> CvBuildingInfo
		""" CvInfo for BuildingID """
	def getCAMERA_FAR_CLIP_Z_HEIGHT( self ) :
		# type: () -> float
		pass
	def getCAMERA_LOWER_PITCH( self ) :
		# type: () -> float
		pass
	def getCAMERA_MAX_TRAVEL_DISTANCE( self ) :
		# type: () -> float
		pass
	def getCAMERA_MAX_TURN_OFFSET( self ) :
		# type: () -> float
		pass
	def getCAMERA_MAX_YAW( self ) :
		# type: () -> float
		pass
	def getCAMERA_MIN_DISTANCE( self ) :
		# type: () -> float
		pass
	def getCAMERA_MIN_YAW( self ) :
		# type: () -> float
		pass
	def getCAMERA_SPECIAL_PITCH( self ) :
		# type: () -> float
		pass
	def getCAMERA_START_DISTANCE( self ) :
		# type: () -> float
		pass
	def getCAMERA_UPPER_PITCH( self ) :
		# type: () -> float
		pass
	def getCITY_HOME_PLOT( self ) :
		# type: () -> int
		pass
	def getCITY_MAX_NUM_BUILDINGS( self ) :
		# type: () -> int
		pass
	def getCalendarInfo( self, arg0 ) :
		# type: (int) -> CvCalendarInfo
		""" Returns Info object """
	def getCitySizeTypes( self ) :
		# type: () -> str
		""" Returns enum string """
	def getCityTabInfo( self, arg0 ) :
		# type: (int) -> CvCityTabInfo
		""" CityTabInfo - () - Returns Info object """
	def getCivicInfo( self, arg0 ) :
		# type: (int) -> CvCivicInfo
		""" CvInfo for CivicID """
	def getCivicOptionInfo( self, arg0 ) :
		# type: (int) -> CvCivicOptionInfo
		""" CvInfo for CivicID """
	def getCivilizationArtInfo( self, arg0 ) :
		# type: (int) -> CvCivilizationArtInfo
		""" CvArtInfo for CivilizationID """
	def getCivilizationInfo( self, arg0 ) :
		# type: (int) -> CvCivilizationInfo
		""" CvInfo for CivilizationID """
	def getClimateInfo( self, arg0 ) :
		# type: (int) -> CvClimateInfo
		""" CvClimateInfo - (ClimateTypeID) """
	def getColorInfo( self, arg0 ) :
		# type: (int) -> CvColorInfo
		pass
	def getCommandInfo( self, arg0 ) :
		# type: (int) -> CvCommandInfo
		""" CvInfo for CommandID """
	def getCommerceInfo( self, arg0 ) :
		# type: (int) -> CvCommerceInfo
		""" CvInfo for CommerceID """
	def getConceptInfo( self, arg0 ) :
		# type: (int) -> CvConceptInfo
		""" Concept Info () - Returns info object """
	def getContactTypes( self ) :
		# type: () -> str
		""" Returns enum string """
	def getControlInfo( self, arg0 ) :
		# type: (int) -> CvControlInfo
		""" CvInfo for ControlID """
	def getCorporationInfo( self, arg0 ) :
		# type: (int) -> CvCorporationInfo
		""" CvInfo for CorporationID """
	def getCultureLevelInfo( self, arg0 ) :
		# type: (int) -> CvCultureLevelInfo
		""" CvInfo for CultureLevelID """
	def getDefineFLOAT( self, arg0 ) :
		# type: (str) -> float
		pass
	def getDefineINT( self, arg0 ) :
		# type: (str) -> int
		pass
	def getDefineSTRING( self, arg0 ) :
		# type: (str) -> str
		pass
	def getDenialInfo( self, arg0 ) :
		# type: (int) -> CvDenialInfo
		""" Returns Info object """
	def getDiplomacyInfo( self, arg0 ) :
		# type: (int) -> CvDiplomacyInfo
		""" CvInfo for DiplomacyID """
	def getDiplomacyPowerTypes( self ) :
		# type: () -> str
		""" Returns enum string """
	def getDomainInfo( self, arg0 ) :
		# type: (int) -> CvDomainInfo
		""" CvInfo for DomainID """
	def getEVENT_MESSAGE_TIME( self ) :
		# type: () -> int
		pass
	def getEffectInfo( self, arg0 ) :
		# type: (int) -> CvEffectInfo
		""" CvInfo for EffectID """
	def getEmphasizeInfo( self, arg0 ) :
		# type: (int) -> CvEmphasizeInfo
		""" CvInfo for EmphasizeID """
	def getEntityEventType( self ) :
		# type: () -> str
		""" Returns enum string """
	def getEraInfo( self, arg0 ) :
		# type: (int) -> CvEraInfo
		pass
	def getEspionageMissionInfo( self, arg0 ) :
		# type: (int) -> CvEspionageMissionInfo
		""" Returns info object """
	def getEventInfo( self, arg0 ) :
		# type: (int) -> CvEventInfo
		""" Returns info object """
	def getEventTriggerInfo( self, arg0 ) :
		# type: (int) -> CvEventTriggerInfo
		""" Returns info object """
	def getFEATURE_GROWTH_MODIFIER( self ) :
		# type: () -> int
		pass
	def getFIELD_OF_VIEW( self ) :
		# type: () -> float
		pass
	def getFOOD_CONSUMPTION_PER_POPULATION( self ) :
		# type: () -> int
		pass
	def getFORTIFY_MODIFIER_PER_TURN( self ) :
		# type: () -> int
		pass
	def getFeatureArtInfo( self, arg0 ) :
		# type: (int) -> CvFeatureArtInfo
		""" Returns info object """
	def getFeatureInfo( self, arg0 ) :
		# type: (int) -> CvFeatureInfo
		""" CvInfo for FeatureID """
	def getFlavorTypes( self ) :
		# type: () -> str
		""" Returns enum string """
	def getForceControlInfo( self, arg0 ) :
		# type: (int) -> CvForceControlInfo
		""" Returns Info object """
	def getFunctionTypes( self ) :
		# type: () -> str
		""" Returns enum string """
	def getGame( self ) :
		# type: () -> Any
		""" CyGame() """
	def getGameOptionInfo( self, arg0 ) :
		# type: (int) -> CvGameOptionInfo
		""" Returns Info object """
	def getGameSpeedInfo( self, arg0 ) :
		# type: (int) -> CvGameSpeedInfo
		""" CvInfo for GameSpeedID """
	def getGoodyInfo( self, arg0 ) :
		# type: (int) -> CvGoodyInfo
		""" CvInfo for GoodyID """
	def getGraphicOptionsInfo( self, arg0 ) :
		# type: (int) -> CvGraphicOptionsInfo
		""" GraphicOptionsInfo for GraphicOptionsInfo """
	def getGraphicOptionsInfoByIndex( self, GraphicOptionsInfoID ) :
		# type: (Any) -> Any
		""" GraphicOptionsInfo for GraphicOptionsInfo """
	def getHILLS_EXTRA_DEFENSE( self ) :
		# type: () -> int
		pass
	def getHILLS_EXTRA_MOVEMENT( self ) :
		# type: () -> int
		pass
	def getHILLS_SEE_FROM_CHANGE( self ) :
		# type: () -> int
		pass
	def getHILLS_SEE_THROUGH_CHANGE( self ) :
		# type: () -> int
		pass
	def getHandicapInfo( self, arg0 ) :
		# type: (int) -> CvHandicapInfo
		""" CvInfo for HandicapID """
	def getHints( self ) :
		# type: () -> Hints
		""" Returns info object """
	def getHurryInfo( self, arg0 ) :
		# type: (int) -> CvHurryInfo
		""" CvInfo for HurryID """
	def getINVALID_PLOT_COORD( self ) :
		# type: () -> int
		pass
	def getImprovementArtInfo( self, arg0 ) :
		# type: (int) -> CvImprovementArtInfo
		""" Returns info object """
	def getImprovementInfo( self, arg0 ) :
		# type: (int) -> CvImprovementInfo
		""" CvInfo for ImprovementID """
	def getInfoTypeForString( self, arg0 ) :
		# type: (str) -> int
		""" returns the info index with the matching type string """
	def getInterfaceArtInfo( self, arg0 ) :
		# type: (int) -> CvInterfaceArtInfo
		""" CvArtInfo for InterfaceArtID """
	def getLAKE_MAX_AREA_SIZE( self ) :
		# type: () -> int
		pass
	def getLeaderHeadInfo( self, arg0 ) :
		# type: (int) -> CvLeaderHeadInfo
		""" CvInfo for LeaderHeadID """
	def getLeaderheadArtInfo( self, arg0 ) :
		# type: (int) -> CvLeaderheadArtInfo
		""" CvArtInfo for LeaderheadID """
	def getMAX_CITY_DEFENSE_DAMAGE( self ) :
		# type: () -> int
		pass
	def getMAX_CIV_PLAYERS( self ) :
		# type: () -> int
		pass
	def getMAX_CIV_TEAMS( self ) :
		# type: () -> int
		pass
	def getMAX_HIT_POINTS( self ) :
		# type: () -> int
		pass
	def getMAX_PLAYERS( self ) :
		# type: () -> int
		pass
	def getMAX_PLOT_LIST_ROWS( self ) :
		# type: () -> int
		pass
	def getMAX_TEAMS( self ) :
		# type: () -> int
		pass
	def getMIN_CITY_RANGE( self ) :
		# type: () -> int
		pass
	def getMIN_WATER_SIZE_FOR_OCEAN( self ) :
		# type: () -> int
		pass
	def getMOVE_DENOMINATOR( self ) :
		# type: () -> int
		pass
	def getMPOptionInfo( self, arg0 ) :
		# type: (int) -> CvMPOptionInfo
		""" Returns Info object """
	def getMainMenus( self ) :
		# type: () -> MainMenus
		""" Returns info object """
	def getMap( self ) :
		# type: () -> CyMap
		""" CyMap() """
	def getMemoryInfo( self, arg0 ) :
		# type: (int) -> CvMemoryInfo
		pass
	def getMiscArtInfo( self, arg0 ) :
		# type: (int) -> CvMiscArtInfo
		""" CvArtInfo for MiscArtID """
	def getMissionInfo( self, arg0 ) :
		# type: (int) -> CvMissionInfo
		""" CvInfo for MissionID """
	def getMonthInfo( self, arg0 ) :
		# type: (int) -> CvMonthInfo
		""" Returns Info object """
	def getMovieArtInfo( self, arg0 ) :
		# type: (int) -> CvMovieArtInfo
		""" CvArtInfo for MovieArtID """
	def getNUM_AND_TECH_PREREQS( self ) :
		# type: () -> int
		pass
	def getNUM_BUILDING_AND_TECH_PREREQS( self ) :
		# type: () -> int
		pass
	def getNUM_BUILDING_PREREQ_OR_BONUSES( self ) :
		# type: () -> int
		pass
	def getNUM_CITY_PLOTS( self ) :
		# type: () -> int
		pass
	def getNUM_CORPORATION_PREREQ_BONUSES( self ) :
		# type: () -> int
		pass
	def getNUM_OR_TECH_PREREQS( self ) :
		# type: () -> int
		pass
	def getNUM_ROUTE_PREREQ_OR_BONUSES( self ) :
		# type: () -> int
		pass
	def getNUM_UNIT_AND_TECH_PREREQS( self ) :
		# type: () -> int
		pass
	def getNUM_UNIT_PREREQ_OR_BONUSES( self ) :
		# type: () -> int
		pass
	def getNewConceptInfo( self, arg0 ) :
		# type: (int) -> CvNewConceptInfo
		""" New Concept Info () - Returns info object """
	def getNumActionInfos( self ) :
		# type: () -> int
		""" Total Action Infos XML\Units\CIV4ActionInfos.xml """
	def getNumAnimationOperatorTypes( self ) :
		# type: () -> int
		""" Returns number of AnimationOperatorTypes """
	def getNumArtStyleTypes( self ) :
		# type: () -> int
		""" Returns number of ArtStyleTypes """
	def getNumAutomateInfos( self ) :
		# type: () -> int
		""" Total Automate Infos XML\Units\CIV4AutomateInfos.xml """
	def getNumBonusArtInfos( self ) :
		# type: () -> int
		""" Returns number of BonusArtInfos """
	def getNumBonusInfos( self ) :
		# type: () -> int
		""" Total Bonus Infos XML\Terrain\CIV4BonusInfos.xml """
	def getNumBuildInfos( self ) :
		# type: () -> int
		""" Total Build Infos XML\Units\CIV4BuildInfos.xml """
	def getNumBuildingArtInfos( self ) :
		# type: () -> int
		""" Returns number of BuildingArtInfos """
	def getNumBuildingClassInfos( self ) :
		# type: () -> int
		""" Total Building Class Infos XML\Buildings\CIV4BuildingClassInfos.xml """
	def getNumBuildingInfos( self ) :
		# type: () -> int
		""" Total Building Infos XML\Buildings\CIV4BuildingInfos.xml """
	def getNumCalendarInfos( self ) :
		# type: () -> int
		""" Returns NumCalendarInfos """
	def getNumCitySizeTypes( self ) :
		# type: () -> int
		""" Returns number of CitySizeTypes """
	def getNumCityTabInfos( self ) :
		# type: () -> int
		""" Returns NumCityTabInfos """
	def getNumCivicInfos( self ) :
		# type: () -> int
		""" Total Civic Infos XML\Misc\CIV4CivicInfos.xml """
	def getNumCivicOptionInfos( self ) :
		# type: () -> int
		""" Total Civic Infos XML\Misc\CIV4CivicOptionInfos.xml """
	def getNumCivilizationArtInfos( self ) :
		# type: () -> int
		""" Returns number of CivilizationArtInfos """
	def getNumCivilizationInfos( self ) :
		# type: () -> int
		""" Total Civilization Infos XML\Civilizations\CIV4CivilizationInfos.xml """
	def getNumClimateInfos( self ) :
		# type: () -> int
		""" Number of climate infos """
	def getNumCommandInfos( self ) :
		# type: () -> int
		""" Total Command Infos XML\Units\CIV4CommandInfos.xml """
	def getNumConceptInfos( self ) :
		# type: () -> int
		""" NumConceptInfos """
	def getNumControlInfos( self ) :
		# type: () -> int
		""" Total Control Infos XML\Units\CIV4ControlInfos.xml """
	def getNumCorporationInfos( self ) :
		# type: () -> int
		""" Total Religion Infos XML\GameInfo\CIV4CorporationInfos.xml """
	def getNumCultureLevelInfos( self ) :
		# type: () -> int
		""" Number of culture level infos """
	def getNumDenialInfos( self ) :
		# type: () -> int
		""" Returns NumDenialInfos """
	def getNumDiplomacyInfos( self ) :
		# type: () -> int
		""" Total diplomacy Infos XML\GameInfo\CIV4DiplomacyInfos.xml """
	def getNumEffectInfos( self ) :
		# type: () -> int
		""" Number of effect infos """
	def getNumEmphasizeInfos( self ) :
		# type: () -> int
		""" Total EmphasizeInfos """
	def getNumEntityEventTypes( self ) :
		# type: () -> int
		""" Returns number of EntityEventTypes """
	def getNumEraInfos( self ) :
		# type: () -> int
		""" Number of era infos """
	def getNumEspionageMissionInfos( self ) :
		# type: () -> int
		""" Returns number of EspionageMissionInfos """
	def getNumEventInfos( self ) :
		# type: () -> int
		""" Returns number of EventInfos """
	def getNumEventTriggerInfos( self ) :
		# type: () -> int
		""" Returns number of EventTriggerInfos """
	def getNumFeatureArtInfos( self ) :
		# type: () -> int
		""" Returns number of FeatureArtInfos """
	def getNumFeatureInfos( self ) :
		# type: () -> int
		""" Total Feature Infos XML\Terrain\CIV4FeatureInfos.xml """
	def getNumFlavorTypes( self ) :
		# type: () -> int
		""" Returns number of FlavorTypes """
	def getNumForceControlInfos( self ) :
		# type: () -> int
		""" Returns NumForceControlInfos """
	def getNumGameOptionInfos( self ) :
		# type: () -> int
		""" Returns NumGameOptionInfos """
	def getNumGameSpeedInfos( self ) :
		# type: () -> int
		""" Total Game speed Infos XML\GameInfo\CIV4GameSpeedInfo.xml """
	def getNumGoodyInfos( self ) :
		# type: () -> int
		""" Total Goody Infos XML\GameInfo\CIV4GoodyInfos.xml """
	def getNumHandicapInfos( self ) :
		# type: () -> int
		""" Total Handicap Infos XML\GameInfo\CIV4HandicapInfos.xml """
	def getNumHints( self ) :
		# type: () -> int
		""" Returns number of Hints """
	def getNumHurryInfos( self ) :
		# type: () -> int
		""" Total Hurry Infos """
	def getNumImprovementArtInfos( self ) :
		# type: () -> int
		""" Returns number of ImprovementArtInfos """
	def getNumImprovementInfos( self ) :
		# type: () -> int
		""" Total Improvement Infos XML\Terrain\CIV4ImprovementInfos.xml """
	def getNumInterfaceArtInfos( self ) :
		# type: () -> int
		""" Total InterfaceArtnology Infos XML\InterfaceArtnologies\CIV4InterfaceArtInfos.xml """
	def getNumLeaderHeadInfos( self ) :
		# type: () -> int
		""" Total LeaderHead Infos XML\Civilizations\CIV4LeaderHeadInfos.xml """
	def getNumLeaderheadArtInfos( self ) :
		# type: () -> int
		""" Returns number of LeaderHeadArtInfos """
	def getNumMPOptionInfos( self ) :
		# type: () -> int
		""" Returns NumMPOptionInfos """
	def getNumMainMenus( self ) :
		# type: () -> int
		""" Returns number """
	def getNumMiscArtInfos( self ) :
		# type: () -> int
		""" Total MiscArtnology Infos XML\MiscArt\CIV4MiscArtInfos.xml """
	def getNumMissionInfos( self ) :
		# type: () -> int
		""" Total Mission Infos XML\Units\CIV4MissionInfos.xml """
	def getNumMonthInfos( self ) :
		# type: () -> int
		""" Returns NumMonthInfos """
	def getNumMovieArtInfos( self ) :
		# type: () -> int
		""" Total MovieArt Infos XML\MovieArtInfos\CIV4ArtDefines.xml """
	def getNumNewConceptInfos( self ) :
		# type: () -> int
		""" NumNewConceptInfos """
	def getNumPlayableCivilizationInfos( self ) :
		# type: () -> int
		""" Total # of Playable Civs """
	def getNumPlayerColorInfos( self ) :
		# type: () -> int
		""" Returns number of PlayerColorInfos """
	def getNumPlayerOptionInfos( self ) :
		# type: () -> int
		pass
	def getNumProcessInfos( self ) :
		# type: () -> int
		""" Total ProcessInfos """
	def getNumProjectInfos( self ) :
		# type: () -> int
		""" Total Project Infos XML\GameInfo\CIV4ProjectInfos.xml """
	def getNumPromotionInfos( self ) :
		# type: () -> int
		""" Total Promotion Infos XML\Units\CIV4PromotionInfos.xml """
	def getNumQuestInfos( self ) :
		# type: () -> int
		""" Returns number of QuestInfos """
	def getNumReligionInfos( self ) :
		# type: () -> int
		""" Total Religion Infos XML\GameInfo\CIV4ReligionInfos.xml """
	def getNumRouteInfos( self ) :
		# type: () -> int
		""" Total Route Infos XML\Misc\CIV4RouteInfos.xml """
	def getNumSeaLevelInfos( self ) :
		# type: () -> int
		""" Number of seal level infos """
	def getNumSeasonInfos( self ) :
		# type: () -> int
		""" Returns NumSeasonInfos """
	def getNumSpecialBuildingInfos( self ) :
		# type: () -> int
		""" Total Special Building Infos """
	def getNumSpecialUnitInfos( self ) :
		# type: () -> int
		""" Total SpecialUnit Infos XML\Units\CIV4SpecialUnitInfos.xml """
	def getNumSpecialistInfos( self ) :
		# type: () -> int
		""" Total Specialist Infos XML\Units\CIV4SpecialistInfos.xml """
	def getNumTechInfos( self ) :
		# type: () -> int
		""" Total Technology Infos XML\Technologies\CIV4TechInfos.xml """
	def getNumTerrainArtInfos( self ) :
		# type: () -> int
		""" Returns number of TerrainArtInfos """
	def getNumTerrainInfos( self ) :
		# type: () -> int
		""" Total Terrain Infos XML\Terrain\CIV4TerrainInfos.xml """
	def getNumTraitInfos( self ) :
		# type: () -> int
		""" Total Civilization Infos XML\Civilizations\CIV4TraitInfos.xml """
	def getNumTurnTimerInfos( self ) :
		# type: () -> int
		""" Total Turn timer Infos XML\GameInfo\CIV4TurnTimerInfo.xml """
	def getNumTutorialInfos( self ) :
		# type: () -> int
		""" Returns number of TutorialInfos """
	def getNumUnitArtInfos( self ) :
		# type: () -> int
		""" Total UnitArtnology Infos XML\UnitArt\CIV4UnitArtInfos.xml """
	def getNumUnitArtStyleTypeInfos( self ) :
		# type: () -> int
		""" Returns number of UnitArtStyleTypes """
	def getNumUnitClassInfos( self ) :
		# type: () -> int
		""" Total Unit Class Infos XML\Units\CIV4UnitClassInfos.xml """
	def getNumUnitCombatInfos( self ) :
		# type: () -> int
		""" Total Unit Combat Infos XML\Units\CIV4UnitCombatInfos.xml """
	def getNumUnitInfos( self ) :
		# type: () -> int
		""" Total Unit Infos XML\Units\CIV4UnitInfos.xml """
	def getNumUpkeepInfos( self ) :
		# type: () -> int
		""" Number of upkeep infos """
	def getNumVictoryInfos( self ) :
		# type: () -> int
		""" Total Victory Infos XML\GameInfo\CIV4VictoryInfos.xml """
	def getNumVoteInfos( self ) :
		# type: () -> int
		""" Total VoteInfos """
	def getNumVoteSourceInfos( self ) :
		# type: () -> int
		pass
	def getNumWorldInfos( self ) :
		# type: () -> int
		""" Number of world infos """
	def getPEAK_SEE_FROM_CHANGE( self ) :
		# type: () -> int
		pass
	def getPEAK_SEE_THROUGH_CHANGE( self ) :
		# type: () -> int
		pass
	def getPERCENT_ANGER_DIVISOR( self ) :
		# type: () -> int
		pass
	def getPLOT_SIZE( self ) :
		# type: () -> float
		pass
	def getPlayer( self, arg0 ) :
		# type: (int) -> CyPlayer
		""" iPlayer instance """
	def getPlayerColorInfo( self, arg0 ) :
		# type: (int) -> CvPlayerColorInfo
		pass
	def getPlayerOptionsInfo( self, arg0 ) :
		# type: (int) -> CvPlayerOptionsInfo
		""" PlayerOptionsInfo for PlayerOptionsInfo """
	def getPlayerOptionsInfoByIndex( self, PlayerOptionsInfoID ) :
		# type: (Any) -> Any
		""" PlayerOptionsInfo for PlayerOptionsInfo """
	def getProcessInfo( self, arg0 ) :
		# type: (int) -> CvProcessInfo
		""" CvInfo for ProcessID """
	def getProjectInfo( self, arg0 ) :
		# type: (int) -> CvProjectInfo
		""" CvInfo for ProjectID """
	def getPromotionInfo( self, arg0 ) :
		# type: (int) -> CvPromotionInfo
		""" CvInfo for PromotionID """
	def getQuestInfo( self, arg0 ) :
		# type: (int) -> CvQuestInfo
		""" Returns info object """
	def getRIVER_ATTACK_MODIFIER( self ) :
		# type: () -> int
		pass
	def getROUTE_FEATURE_GROWTH_MODIFIER( self ) :
		# type: () -> int
		pass
	def getReligionInfo( self, arg0 ) :
		# type: (int) -> CvReligionInfo
		""" CvInfo for ReligionID """
	def getRouteInfo( self, arg0 ) :
		# type: (int) -> CvRouteInfo
		""" CvInfo for RouteID """
	def getSEAWATER_SEE_FROM_CHANGE( self ) :
		# type: () -> int
		pass
	def getSHADOW_SCALE( self ) :
		# type: () -> float
		pass
	def getSeaLevelInfo( self, arg0 ) :
		# type: (int) -> CvSeaLevelInfo
		""" CvSeaLevelInfo - (SeaLevelTypeID) """
	def getSeasonInfo( self, arg0 ) :
		# type: (int) -> CvSeasonInfo
		""" Returns Info object """
	def getSpecialBuildingInfo( self, arg0 ) :
		# type: (int) -> CvSpecialBuildingInfo
		""" CvInfo for SpecialBuildingID """
	def getSpecialUnitInfo( self, arg0 ) :
		# type: (int) -> CvSpecialUnitInfo
		""" CvInfo for UnitID """
	def getSpecialistInfo( self, arg0 ) :
		# type: (int) -> CvSpecialistInfo
		""" CvInfo for SpecialistID """
	def getTeam( self, arg0 ) :
		# type: (int) -> CyTeam
		""" iTeam instance """
	def getTechInfo( self, arg0 ) :
		# type: (int) -> CvTechInfo
		""" CvInfo for TechID """
	def getTerrainArtInfo( self, arg0 ) :
		# type: (int) -> CvTerrainArtInfo
		""" Returns info object """
	def getTerrainInfo( self, arg0 ) :
		# type: (int) -> CvTerrainInfo
		""" CvInfo for TerrainID """
	def getTraitInfo( self, arg0 ) :
		# type: (int) -> CvTraitInfo
		""" CvInfo for TraitID """
	def getTurnTimerInfo( self, arg0 ) :
		# type: (int) -> CvTurnTimerInfo
		""" CvInfo for TurnTimerID """
	def getTutorialInfo( self, arg0 ) :
		# type: (int) -> CvTutorialInfo
		""" Returns info object """
	def getTypesEnum( self, arg0 ) :
		# type: (str) -> int
		""" returns the type enum from a type string """
	def getUNIT_MULTISELECT_DISTANCE( self ) :
		# type: () -> float
		pass
	def getUNIT_MULTISELECT_MAX( self ) :
		# type: () -> int
		pass
	def getUSE_SPIES_NO_ENTER_BORDERS( self ) :
		# type: () -> int
		pass
	def getUnitAIInfo( self, arg0 ) :
		# type: (int) -> CvUnitAIInfo
		pass
	def getUnitArtInfo( self, arg0 ) :
		# type: (int) -> CvUnitArtInfo
		""" CvArtInfo for UnitID """
	def getUnitArtStyleTypeInfo( self, arg0 ) :
		# type: (int) -> CvUnitArtStyleTypeInfo
		""" CvInfo for UnitArtStyleTypeID """
	def getUnitClassInfo( self, arg0 ) :
		# type: (int) -> CvUnitClassInfo
		""" CvInfo for UnitClassID """
	def getUnitCombatInfo( self, arg0 ) :
		# type: (int) -> CvUnitCombatInfo
		""" CvInfo for UnitCombatID """
	def getUnitInfo( self, arg0 ) :
		# type: (int) -> CvUnitInfo
		""" CvInfo for UnitID """
	def getUpkeepInfo( self, arg0 ) :
		# type: (int) -> CvUpkeepInfo
		""" CvInfo for upkeep info """
	def getVictoryInfo( self, arg0 ) :
		# type: (int) -> CvVictoryInfo
		""" CvInfo for VictoryID """
	def getVoteInfo( self, arg0 ) :
		# type: (int) -> CvVoteInfo
		""" CvInfo for VoteID """
	def getVoteSourceInfo( self, arg0 ) :
		# type: (int) -> CvVoteSourceInfo
		""" Returns info object """
	def getWorldInfo( self, arg0 ) :
		# type: (int) -> CvWorldInfo
		""" CvWorldInfo - (WorldTypeID) """
	def getYieldInfo( self, arg0 ) :
		# type: (int) -> CvYieldInfo
		""" CvInfo for YieldID """
	def isDebugBuild( self ) :
		# type: () -> Any
		""" returns true if running a debug build """
	def setDefineFLOAT( self, arg0, arg1 ) :
		# type: (str, float) -> None
		pass
	def setDefineINT( self, arg0, arg1 ) :
		# type: (str, int) -> None
		pass
	def setDefineSTRING( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass

class CyGlobeLayer( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButtonStyle( self ) :
		# type: () -> char
		pass
	def getCurrentOption( self ) :
		# type: () -> int
		pass
	def getName( self ) :
		# type: () -> char
		pass
	def getNumOptions( self, *args, **kwargs ) :
		""" int getNumLayers() """
	def getOptionName( self, arg0 ) :
		# type: (int) -> unicode
		pass
	def isGlobeviewRequired( self ) :
		# type: () -> bool
		pass
	def isNone( self ) :
		# type: () -> bool
		pass
	def shouldCitiesZoom( self ) :
		# type: () -> bool
		pass

class CyGlobeLayerManager( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getCurrentLayer( self, *args, **kwargs ) :
		""" CvGlobeLayer* getCurrentLayer """
	def getCurrentLayerID( self ) :
		# type: () -> int
		pass
	def getCurrentLayerName( self ) :
		# type: () -> TCHAR
		pass
	def getLayer( self, arg0 ) :
		# type: (int) -> CvGlobeLayer
		pass
	def getLayerID( self, *args, **kwargs ) :
		""" int getLayerID(const TCHAR*) """
	def getNumLayers( self ) :
		# type: () -> int
		pass
	def setCurrentLayer( self ) :
		# type: () -> None
		pass

class CyHallOfFameInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getNumGames( self ) :
		# type: () -> int
		pass
	def getReplayInfo( self, arg0 ) :
		# type: (int) -> CyReplayInfo
		pass
	def loadReplays( self ) :
		# type: () -> None
		pass

class CyInterface( object ) :
	def DoSoundtrack( self, arg0 ) :
		# type: (str) -> bool
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	def addCombatMessage( self, arg0, arg1 ) :
		# type: (int, unicode) -> None
		pass
	def addImmediateMessage( self, arg0, arg1 ) :
		# type: (unicode, str) -> None
		pass
	def addMessage( self, *args, **kwargs ) :
		""" void (int /*PlayerTypes*/ ePlayer, bool bForce, int iLength, wstring szString, string szSound = NULL, int /*InterfaceMessageTypes*/ eType = MESSAGE_TYPE_INFO, string szIcon = NULL, ColorTypes eFlashColor = NO_COLOR, int iFlashX = -1, int iFlashY = -1, bool bShowOffScreenArrows = false, bool bShowOnScreenArrows = false) """
	def addQuestMessage( self, arg0, arg1 ) :
		# type: (int, unicode) -> None
		pass
	def addSelectedCity( self, arg0 ) :
		# type: (CyCity) -> None
		pass
	def cacheInterfacePlotUnits( self, *args, **kwargs ) :
		""" void (CyPlot *) """
	def canCreateGroup( self ) :
		# type: () -> bool
		pass
	def canDeleteGroup( self ) :
		# type: () -> bool
		pass
	def canHandleAction( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def canSelectHeadUnit( self ) :
		# type: () -> bool
		pass
	def checkFlashReset( self, arg0 ) :
		# type: (int) -> None
		pass
	def checkFlashUpdate( self ) :
		# type: () -> bool
		pass
	def clearSelectedCities( self ) :
		# type: () -> None
		pass
	def clearSelectionList( self ) :
		# type: () -> None
		pass
	def countEntities( self, arg0 ) :
		# type: (int) -> int
		pass
	def determineWidth( self, arg0 ) :
		# type: (unicode) -> int
		pass
	def doPing( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def endTimer( self, arg0 ) :
		# type: (str) -> None
		pass
	def exitingToMainMenu( self, arg0 ) :
		# type: (str) -> None
		pass
	def getActionsToShow( self ) :
		# type: () -> tuple
		pass
	def getCachedInterfacePlotUnit( self, index ) :
		# type: (Any) -> CyUnit
		pass
	def getCityTabSelectionRow( self ) :
		# type: () -> int
		pass
	def getCursorPlot( self ) :
		# type: () -> CyPlot
		pass
	def getEndTurnState( self ) :
		# type: () -> EndTurnButtonStates
		pass
	def getGotoPlot( self ) :
		# type: () -> CyPlot
		pass
	def getHeadSelectedCity( self ) :
		# type: () -> CyCity
		pass
	def getHeadSelectedUnit( self ) :
		# type: () -> CyUnit
		pass
	def getHelpString( self ) :
		# type: () -> unicode
		pass
	def getHighlightPlot( self ) :
		# type: () -> CyPlot
		pass
	def getInterfaceMode( self ) :
		# type: () -> int
		pass
	def getInterfacePlotUnit( self ) :
		# type: () -> CyUnit
		pass
	def getLengthSelectionList( self ) :
		# type: () -> int
		pass
	def getMouseOverPlot( self ) :
		# type: () -> CyPlot
		pass
	def getMousePos( self ) :
		# type: () -> POINT
		""" returns the mouse coords """
	def getNumCachedInterfacePlotUnits( self ) :
		# type: () -> int
		pass
	def getNumOrdersQueued( self ) :
		# type: () -> int
		pass
	def getNumVisibleUnits( self ) :
		# type: () -> int
		pass
	def getOrderNodeData1( self, arg0 ) :
		# type: (int) -> int
		pass
	def getOrderNodeData2( self, arg0 ) :
		# type: (int) -> int
		pass
	def getOrderNodeSave( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getOrderNodeType( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPlotListColumn( self ) :
		# type: () -> int
		pass
	def getPlotListOffset( self ) :
		# type: () -> int
		pass
	def getSelectionPlot( self ) :
		# type: () -> CyPlot
		pass
	def getSelectionUnit( self ) :
		# type: () -> CyUnit
		pass
	def getShowInterface( self ) :
		# type: () -> InterfaceVisibility
		pass
	def insertIntoSelectionList( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (CyUnit, bool, bool, bool, bool) -> None
		pass
	def isCityScreenUp( self ) :
		# type: () -> bool
		pass
	def isCitySelected( self, arg0 ) :
		# type: (CyCity) -> bool
		pass
	def isCitySelection( self ) :
		# type: () -> bool
		pass
	def isDirty( self, arg0 ) :
		# type: (InterfaceDirtyBits) -> bool
		pass
	def isFlashing( self ) :
		# type: () -> bool
		pass
	def isFlashingPlayer( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isFocused( self ) :
		# type: () -> bool
		pass
	def isFocusedWidget( self ) :
		# type: () -> bool
		pass
	def isInAdvancedStart( self ) :
		# type: () -> bool
		pass
	def isInMainMenu( self ) :
		# type: () -> bool
		pass
	def isLeftMouseDown( self ) :
		# type: () -> bool
		pass
	def isNetStatsVisible( self ) :
		# type: () -> bool
		pass
	def isOOSVisible( self ) :
		# type: () -> bool
		pass
	def isOneCitySelected( self ) :
		# type: () -> bool
		pass
	def isRightMouseDown( self ) :
		# type: () -> bool
		pass
	def isScoresMinimized( self ) :
		# type: () -> bool
		pass
	def isScoresVisible( self ) :
		# type: () -> bool
		pass
	def isScreenUp( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isUnitFocus( self ) :
		# type: () -> bool
		pass
	def isYieldVisibleMode( self ) :
		# type: () -> bool
		pass
	def lookAtCityBuilding( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def lookAtCityOffset( self, arg0 ) :
		# type: (int) -> None
		pass
	def makeInterfaceDirty( self ) :
		# type: () -> None
		pass
	def mirrorsSelectionGroup( self ) :
		# type: () -> bool
		pass
	def noTechSplash( self ) :
		# type: () -> bool
		pass
	def playAdvisorSound( self, arg0 ) :
		# type: (str) -> None
		pass
	def playGeneralSound( self, arg0 ) :
		# type: (str) -> None
		pass
	def playGeneralSoundAtPlot( self, arg0, arg1 ) :
		# type: (int, CyPlot) -> None
		pass
	def playGeneralSoundByID( self, arg0 ) :
		# type: (int) -> None
		pass
	def removeFromSelectionList( self, arg0 ) :
		# type: (CyUnit) -> None
		pass
	def selectAll( self, arg0 ) :
		# type: (CyPlot) -> None
		pass
	def selectCity( self, arg0, arg1 ) :
		# type: (CyCity, bool) -> None
		pass
	def selectGroup( self, arg0, arg1, arg2, arg3 ) :
		# type: (CyUnit, bool, bool, bool) -> None
		pass
	def selectHotKeyUnit( self, arg0 ) :
		# type: (int) -> int
		pass
	def selectUnit( self, arg0, arg1, arg2, arg3 ) :
		# type: (CyUnit, bool, bool, bool) -> None
		pass
	def setBusy( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setCityTabSelectionRow( self, arg0 ) :
		# type: (int) -> None
		pass
	def setDirty( self, arg0, arg1 ) :
		# type: (InterfaceDirtyBits, bool) -> None
		pass
	def setInterfaceMode( self, arg0 ) :
		# type: (int) -> None
		pass
	def setPausedPopups( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setShowInterface( self, arg0 ) :
		# type: (InterfaceVisibility) -> None
		pass
	def setSoundSelectionReady( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setWorldBuilder( self, arg0 ) :
		# type: (bool) -> None
		pass
	def shiftKey( self ) :
		# type: () -> bool
		pass
	def shouldDisplayEndTurn( self ) :
		# type: () -> bool
		pass
	def shouldDisplayEndTurnButton( self ) :
		# type: () -> bool
		pass
	def shouldDisplayFlag( self ) :
		# type: () -> bool
		pass
	def shouldDisplayReturn( self ) :
		# type: () -> bool
		pass
	def shouldDisplayUnitModel( self ) :
		# type: () -> bool
		pass
	def shouldDisplayWaitingOthers( self ) :
		# type: () -> bool
		pass
	def shouldDisplayWaitingYou( self ) :
		# type: () -> bool
		pass
	def shouldFlash( self, arg0 ) :
		# type: (int) -> bool
		pass
	def shouldShowAction( self, arg0 ) :
		# type: (int) -> bool
		pass
	def shouldShowResearchButtons( self ) :
		# type: () -> bool
		pass
	def startTimer( self ) :
		# type: () -> None
		pass
	def stop2DSound( self ) :
		# type: () -> None
		pass
	def stopAdvisorSound( self ) :
		# type: () -> None
		pass
	def toggleBareMapMode( self ) :
		# type: () -> None
		pass
	def toggleMusicOn( self ) :
		# type: () -> None
		pass
	def toggleNetStatsVisible( self ) :
		# type: () -> None
		pass
	def toggleScoresMinimized( self ) :
		# type: () -> None
		pass
	def toggleScoresVisible( self ) :
		# type: () -> None
		pass
	def toggleYieldVisibleMode( self ) :
		# type: () -> None
		pass

class CyMap( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def calculatePathDistance( self, *args, **kwargs ) :
		""" finds the shortest passable path between two CyPlots and returns its length, or returns -1 if no such path exists. Note: the path must be all-land or all-water """
	def erasePlots( self ) :
		# type: () -> Any
		""" erases the plots """
	def findBiggestArea( self ) :
		# type: () -> CyArea
		pass
	def findCity( self, *args, **kwargs ) :
		""" CyCity* (int iX, int iY, int (PlayerTypes) eOwner = NO_PLAYER, int (TeamTypes) eTeam = NO_TEAM, bool bSameArea = true, bool bCoastalOnly = false, int (TeamTypes) eTeamAtWarWith = NO_TEAM, int (DirectionTypes) eDirection = NO_DIRECTION, CvCity* pSkipCity = NULL) - finds city """
	def findSelectionGroup( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, int, int, bool, bool) -> CvSelectionGroup
		pass
	def findWater( self, arg0, arg1, arg2 ) :
		# type: (CyPlot, int, bool) -> bool
		pass
	def getArea( self, iID ) :
		# type: (Any) -> CyArea
		""" get CyArea at iID """
	def getBottomLatitude( self ) :
		# type: () -> int
		""" bottom latitude (usually -90) """
	def getClimate( self ) :
		# type: () -> int
		""" climate of the world """
	def getCustomMapOption( self ) :
		# type: () -> int
		""" user defined map setting at this option id """
	def getGridHeight( self ) :
		# type: () -> int
		""" the height of the map, in plots """
	def getGridWidth( self ) :
		# type: () -> int
		""" the width of the map, in plots """
	def getIndexAfterLastArea( self ) :
		# type: () -> int
		""" index for handling NULL areas """
	def getLandPlots( self ) :
		# type: () -> int
		""" total land plots """
	def getMapFractalFlags( self ) :
		# type: () -> int
		pass
	def getMapScriptName( self ) :
		# type: () -> unicode
		""" name of the map script """
	def getNextRiverID( self ) :
		# type: () -> int
		pass
	def getNumAreas( self ) :
		# type: () -> int
		""" total areas """
	def getNumBonuses( self ) :
		# type: () -> int
		""" total bonuses """
	def getNumBonusesOnLand( self ) :
		# type: () -> int
		""" total bonuses on land plots """
	def getNumCustomMapOptions( self ) :
		# type: () -> int
		""" number of custom map settings """
	def getNumLandAreas( self ) :
		# type: () -> int
		""" total land areas """
	def getOwnedPlots( self ) :
		# type: () -> int
		""" total owned plots """
	def getSeaLevel( self ) :
		# type: () -> int
		""" sealevel of the world """
	def getTopLatitude( self ) :
		# type: () -> int
		""" top latitude (usually 90) """
	def getWorldSize( self ) :
		# type: () -> int
		""" size of the world """
	def incrementNextRiverID( self ) :
		# type: () -> None
		pass
	def isNone( self ) :
		# type: () -> bool
		""" valid CyMap() interface """
	def isPlot( self, iX, iY ) :
		# type: (Any, Any) -> bool
		""" is (iX, iY) a valid plot? """
	def isWrapX( self ) :
		# type: () -> bool
		""" whether the map wraps in the X axis """
	def isWrapY( self ) :
		# type: () -> bool
		""" whether the map wraps in the Y axis """
	def numPlots( self ) :
		# type: () -> int
		""" total plots in the map """
	def plot( self, iX, iY ) :
		# type: (Any, Any) -> CyPlot
		""" get CyPlot at (iX,iY) """
	def plotByIndex( self, iIndex ) :
		# type: (Any) -> CyPlot
		""" get a plot by its Index """
	def plotNum( self, iX, iY ) :
		# type: (Any, Any) -> int
		""" the index for a given plot """
	def plotX( self, iIndex ) :
		# type: (Any) -> int
		""" given the index of a plot, returns its X coordinate """
	def plotY( self, iIndex ) :
		# type: (Any) -> int
		""" given the index of a plot, returns its Y coordinate """
	def pointToPlot( self, *args, **kwargs ) :
		pass
	def rebuild( self, *args, **kwargs ) :
		""" used to initialize the map during WorldBuilder load """
	def recalculateAreas( self ) :
		# type: () -> None
		""" Recalculates the areaID for each plot. Should be preceded by CyMap.setPlotTypes(...) """
	def regenerateGameElements( self, *args, **kwargs ) :
		""" used to regenerate everything but the terrain and height maps """
	def resetPathDistance( self ) :
		# type: () -> None
		pass
	def sPlot( self, iX, iY ) :
		# type: (Any, Any) -> CyPlot
		""" static - get CyPlot at (iX,iY) """
	def sPlotByIndex( self, iIndex ) :
		# type: (Any) -> CyPlot
		""" static - get plot by iIndex """
	def setAllPlotTypes( self, arg0 ) :
		# type: (int) -> None
		""" sets all plots to ePlotType """
	def setRevealedPlots( self, arg0, arg1, arg2 ) :
		# type: (int, bool, bool) -> None
		""" reveals the plots to eTeam """
	def syncRandPlot( self, iFlags, iArea, iMinUnitDistance, iTimeout ) :
		# type: (Any, Any, Any, Any) -> CyPlot
		""" random plot based on conditions """
	def updateFog( self ) :
		# type: () -> None
		pass
	def updateMinOriginalStartDist( self, arg0 ) :
		# type: (CyArea) -> None
		pass
	def updateMinimapColor( self ) :
		# type: () -> None
		pass
	def updateVisibility( self ) :
		# type: () -> Any
		""" updates the plots visibility """

class CyMapGenerator( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def addBonuses( self ) :
		# type: () -> None
		pass
	def addFeatures( self ) :
		# type: () -> None
		pass
	def addGameElements( self ) :
		# type: () -> None
		pass
	def addGoodies( self ) :
		# type: () -> None
		pass
	def addLakes( self ) :
		# type: () -> None
		pass
	def addNonUniqueBonusType( self, arg0 ) :
		# type: (int) -> None
		pass
	def addRivers( self ) :
		# type: () -> None
		pass
	def addUniqueBonusType( self, arg0 ) :
		# type: (int) -> None
		pass
	def afterGeneration( self ) :
		# type: () -> None
		pass
	def canPlaceBonusAt( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, int, bool) -> bool
		pass
	def canPlaceGoodyAt( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> bool
		pass
	def doRiver( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> None
		pass
	def eraseBonuses( self ) :
		# type: () -> None
		pass
	def eraseFeatures( self ) :
		# type: () -> None
		pass
	def eraseGoodies( self ) :
		# type: () -> None
		pass
	def eraseRivers( self ) :
		# type: () -> None
		pass
	def generatePlotTypes( self ) :
		# type: () -> None
		pass
	def generateRandomMap( self ) :
		# type: () -> None
		pass
	def generateTerrain( self ) :
		# type: () -> None
		pass
	def isNone( self ) :
		# type: () -> bool
		""" valid CyMapGenerator() interface """
	def setPlotTypes( self, arg0 ) :
		# type: (list) -> None
		""" set plot types to the contents of the given list """

class CyMessageControl( object ) :
	def GetConnState( self, arg0 ) :
		# type: (int) -> int
		pass
	def GetFirstBadConnection( self ) :
		# type: () -> int
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	def sendAdvancedStartAction( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (int, int, int, int, int, bool) -> None
		pass
	def sendConvert( self, arg0 ) :
		# type: (int) -> None
		pass
	def sendDoTask( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (int, int, int, int, bool, bool, bool, bool) -> None
		pass
	def sendEmpireSplit( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def sendEspionageSpendingWeightChange( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def sendModNetMessage( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, int, int, int, int) -> None
		""" This is a NetMessage designed specifically for modders to use to make their mods Multiplayer friendly, eliminating Out-of-Sync errors. Check out 'onModNetMessage()' in CvEventManager for the callback """
	def sendPlayerOption( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def sendPushOrder( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (int, int, int, bool, bool, bool) -> None
		pass
	def sendResearch( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def sendTurnComplete( self ) :
		# type: () -> None
		""" allows you to force a turn to end """
	def sendUpdateCivics( self, arg0 ) :
		# type: (list) -> None
		pass

class CyPlayer( object ) :
	def AI_changeAttitudeExtra( self, arg0, arg1 ) :
		# type: (int, int) -> None
		""" Changes the extra attitude for this player - usually scenario specific """
	def AI_changeMemoryCount( self, *args, **kwargs ) :
		""" void (/*PlayerTypes*/ eIndex1, /*MemoryTypes*/ eIndex2, int iChange) """
	def AI_civicValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def AI_demandRebukedWar( self, arg0 ) :
		# type: (int) -> bool
		pass
	def AI_foundValue( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, int, bool) -> int
		pass
	def AI_getAttitude( self, arg0 ) :
		# type: (int) -> int
		""" Gets the attitude of the player towards the player passed in """
	def AI_getAttitudeExtra( self, arg0 ) :
		# type: (int) -> int
		""" Returns the extra attitude for this player - usually scenario specific """
	def AI_getExtraGoldTarget( self ) :
		# type: () -> int
		pass
	def AI_getMemoryCount( self, *args, **kwargs ) :
		""" int (/*PlayerTypes*/ eIndex1, /*MemoryTypes*/ eIndex2) """
	def AI_getNumAIUnits( self, UnitAIType ) :
		# type: (Any) -> int
		""" Returns # of UnitAITypes the player current has of UnitAIType """
	def AI_isFinancialTrouble( self ) :
		# type: () -> bool
		pass
	def AI_maxGoldPerTurnTrade( self, arg0 ) :
		# type: (int) -> int
		pass
	def AI_maxGoldTrade( self, arg0 ) :
		# type: (int) -> int
		pass
	def AI_setAttitudeExtra( self, arg0, arg1 ) :
		# type: (int, int) -> None
		""" Sets the extra attitude for this player - usually scenario specific """
	def AI_setExtraGoldTarget( self, arg0 ) :
		# type: (int) -> None
		pass
	def AI_totalAreaUnitAIs( self, arg0, arg1 ) :
		# type: (CyArea, int) -> int
		pass
	def AI_totalUnitAIs( self, arg0 ) :
		# type: (int) -> int
		pass
	def AI_totalWaterAreaUnitAIs( self, arg0, arg1 ) :
		# type: (CyArea, int) -> int
		pass
	def AI_unitValue( self, arg0, arg1, arg2 ) :
		# type: (int, int, CyArea) -> int
		pass
	def AI_updateFoundValues( self, arg0 ) :
		# type: (bool) -> None
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	def acquireCity( self, arg0, arg1, arg2 ) :
		# type: (CyCity, bool, bool) -> None
		pass
	def addCityName( self, arg0 ) :
		# type: (unicode) -> None
		pass
	def calculateBaseNetResearch( self ) :
		# type: () -> int
		pass
	def calculateGoldRate( self ) :
		# type: () -> int
		pass
	def calculateInflatedCosts( self ) :
		# type: () -> int
		pass
	def calculateInflationRate( self ) :
		# type: () -> int
		pass
	def calculatePreInflatedCosts( self ) :
		# type: () -> int
		pass
	def calculateResearchModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def calculateResearchRate( self, arg0 ) :
		# type: (int) -> int
		pass
	def calculateTotalCityHappiness( self ) :
		# type: () -> int
		""" Returns the total sum of all city Happiness values """
	def calculateTotalCityHealthiness( self ) :
		# type: () -> int
		""" Returns the total sum of all city Healthiness values """
	def calculateTotalCityUnhappiness( self ) :
		# type: () -> int
		""" Returns the total sum of all city Unhappiness values """
	def calculateTotalCityUnhealthiness( self ) :
		# type: () -> int
		""" Returns the total sum of all city Unhealthiness values """
	def calculateTotalCommerce( self ) :
		# type: () -> int
		pass
	def calculateTotalExports( self, arg0 ) :
		# type: (int) -> int
		""" Returns the total sum of all city gold generated for other civs via trade routes """
	def calculateTotalImports( self, arg0 ) :
		# type: (int) -> int
		""" Returns the total sum of all city gold generated for this civ via trade routes with others """
	def calculateTotalYield( self, arg0 ) :
		# type: (int) -> int
		""" Returns the total sum of all city yield """
	def calculateUnitCost( self ) :
		# type: () -> int
		pass
	def calculateUnitSupply( self ) :
		# type: () -> int
		pass
	def canBuild( self, arg0, arg1, arg2, arg3 ) :
		# type: (CyPlot, int, bool, bool) -> bool
		pass
	def canChangeReligion( self ) :
		# type: () -> bool
		pass
	def canConstruct( self, *args, **kwargs ) :
		""" bool (int /*BuildingTypes*/eBuilding, bool bContinue, bool bTestVisible, bool bIgnoreCost) """
	def canContact( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canConvert( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canCreate( self, arg0, arg1, arg2 ) :
		# type: (int, bool, bool) -> bool
		pass
	def canDoCivics( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canDoEspionageMission( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, CyPlot, int) -> bool
		pass
	def canDoReligion( self, arg0 ) :
		# type: (int) -> int
		pass
	def canEverResearch( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canFound( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def canHaveTradeRoutesWith( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canHurry( self, arg0 ) :
		# type: (int) -> int
		pass
	def canMaintain( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def canRaze( self, arg0 ) :
		# type: (CyCity) -> bool
		pass
	def canReceiveGoody( self, arg0, arg1, arg2 ) :
		# type: (CyPlot, int, CyUnit) -> bool
		pass
	def canResearch( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def canRevolution( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canSplitArea( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canSplitEmpire( self ) :
		# type: () -> bool
		pass
	def canStopTradingWithTeam( self, arg0 ) :
		# type: (int) -> int
		pass
	def canTradeItem( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def canTradeNetworkWith( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canTradeWith( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canTrain( self, arg0, arg1, arg2 ) :
		# type: (int, bool, bool) -> bool
		pass
	def changeAdvancedStartPoints( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeAnarchyTurns( self ) :
		# type: () -> None
		pass
	def changeAssets( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeCoastalTradeRoutes( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeCombatExperience( self, arg0 ) :
		# type: (int) -> None
		""" Combat experience used to produce Warlords """
	def changeCommercePercent( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def changeConscriptCount( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeEspionageSpendingWeightAgainstTeam( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeExtraHappiness( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeGold( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeGoldenAgeTurns( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeNumUnitGoldenAges( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeStateReligionBuildingProductionModifier( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeStateReligionUnitProductionModifier( self, arg0 ) :
		# type: (int) -> None
		pass
	def chooseTech( self, arg0, arg1, arg2 ) :
		# type: (int, unicode, bool) -> None
		pass
	def clearResearchQueue( self ) :
		# type: () -> None
		pass
	def contact( self, arg0 ) :
		# type: (int) -> None
		pass
	def convert( self, arg0 ) :
		# type: (int) -> None
		pass
	def countCityFeatures( self, arg0 ) :
		# type: (int) -> int
		""" Returns ? """
	def countCorporations( self, arg0 ) :
		# type: (int) -> int
		""" Counts the # of corporations this player has """
	def countHeadquarters( self ) :
		# type: () -> int
		""" Counts the # of headquarters this player has """
	def countHolyCities( self ) :
		# type: () -> int
		""" Counts the # of holy cities this player has """
	def countNumBuildings( self, arg0 ) :
		# type: (int) -> int
		""" Returns the number of buildings? """
	def countNumCoastalCities( self ) :
		# type: () -> int
		pass
	def countNumCoastalCitiesByArea( self, *args, **kwargs ) :
		""" (int (CyArea* pArea) """
	def countOwnedBonuses( self, arg0 ) :
		# type: (int) -> int
		pass
	def countPotentialForeignTradeCities( self, arg0 ) :
		# type: (CyArea) -> int
		""" Returns the number of potential foreign trade cities """
	def countPotentialForeignTradeCitiesConnected( self ) :
		# type: () -> int
		""" Returns the number of potential foreign trade cities which are also connected to this player's capital """
	def countTotalCulture( self ) :
		# type: () -> int
		pass
	def countTotalHasCorporation( self ) :
		# type: () -> int
		pass
	def countTotalHasReligion( self ) :
		# type: () -> int
		pass
	def countUnimprovedBonuses( self, *args, **kwargs ) :
		""" int (int (CyArea* pArea, CyPlot* pFromPlot) -  """
	def createGreatPeople( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, bool, int, int) -> None
		pass
	def disband( self, arg0 ) :
		# type: (CyCity) -> None
		pass
	def disbandUnit( self, arg0 ) :
		# type: (bool) -> None
		pass
	def doEspionageMission( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, int, CyPlot, int, CyUnit) -> None
		pass
	def doGoody( self, arg0, arg1 ) :
		# type: (CyPlot, CyUnit) -> None
		pass
	def findBestFoundValue( self ) :
		# type: () -> int
		""" Finds best found value """
	def findHighestHasReligionCount( self ) :
		# type: () -> int
		pass
	def findNewCapital( self ) :
		# type: () -> None
		pass
	def findPathLength( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def findStartingPlot( self, arg0 ) :
		# type: (bool) -> Any
		""" Finds a starting plot for player """
	def firstCity( self, *args, **kwargs ) :
		""" tuple(CyCity, int iterOut) (bool bReverse) - gets the first city """
	def firstSelectionGroup( self, *args, **kwargs ) :
		""" tuple(CySelectionGroup, int iterOut) (bool bReverse) - gets the first selectionGroup """
	def firstUnit( self, *args, **kwargs ) :
		""" tuple(CyUnit, int iterOut) (bool bReverse) - gets the first unit """
	def forcePeace( self, arg0 ) :
		# type: (int) -> None
		pass
	def found( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def foundCorporation( self, arg0 ) :
		# type: (int) -> None
		pass
	def foundReligion( self, arg0, arg1, arg2 ) :
		# type: (int, int, bool) -> None
		pass
	def getAdvancedStartBuildingCost( self, arg0, arg1, arg2 ) :
		# type: (int, bool, CyCity) -> int
		pass
	def getAdvancedStartCityCost( self, *args, **kwargs ) :
		""" int (int (bool bAdd, CyPlot* pPlot) """
	def getAdvancedStartCultureCost( self, *args, **kwargs ) :
		""" int (int (bool bAdd, CyCity* pCity) """
	def getAdvancedStartImprovementCost( self, arg0, arg1, arg2 ) :
		# type: (int, bool, CyPlot) -> int
		pass
	def getAdvancedStartPoints( self ) :
		# type: () -> int
		pass
	def getAdvancedStartPopCost( self, *args, **kwargs ) :
		""" int (int (bool bAdd, CyCity* pCity) """
	def getAdvancedStartRouteCost( self, arg0, arg1, arg2 ) :
		# type: (int, bool, CyPlot) -> int
		pass
	def getAdvancedStartTechCost( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def getAdvancedStartUnitCost( self, arg0, arg1, arg2 ) :
		# type: (int, bool, CyPlot) -> int
		pass
	def getAdvancedStartVisibilityCost( self, arg0, arg1 ) :
		# type: (bool, CyPlot) -> int
		pass
	def getAgricultureHistory( self, arg0 ) :
		# type: (int) -> int
		pass
	def getAnarchyModifier( self ) :
		# type: () -> int
		pass
	def getAnarchyTurns( self ) :
		# type: () -> int
		pass
	def getArtStyleType( self ) :
		# type: () -> int
		""" Returns the ArtStyleType for this player (e.g. European) """
	def getAssets( self ) :
		# type: () -> int
		pass
	def getAveragePopulation( self ) :
		# type: () -> int
		pass
	def getBaseFreeMilitaryUnits( self ) :
		# type: () -> int
		pass
	def getBaseFreeUnits( self ) :
		# type: () -> int
		pass
	def getBestAttackUnitKey( self ) :
		# type: () -> str
		""" returns the name of the best attack unit """
	def getBestAttackUnitName( self ) :
		# type: () -> str
		""" returns the name of the best attack unit """
	def getBonusExport( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBonusImport( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingBadHealth( self ) :
		# type: () -> int
		pass
	def getBuildingClassCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingClassCountPlusMaking( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingClassMaking( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingClassPrereqBuilding( self, arg0, arg1, iExtra ) :
		# type: (int, int, Any) -> int
		pass
	def getBuildingGoodHealth( self ) :
		# type: () -> int
		pass
	def getBuildingHappiness( self ) :
		# type: () -> int
		pass
	def getBuildingProductionNeeded( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCapitalCity( self, arg0 ) :
		# type: (int) -> CyCity
		pass
	def getCapitalCommerceRateModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCapitalYieldRateModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCitiesLost( self ) :
		# type: () -> int
		pass
	def getCity( self, arg0 ) :
		# type: (int) -> CyCity
		pass
	def getCityDefenseModifier( self ) :
		# type: () -> int
		pass
	def getCityName( self, arg0 ) :
		# type: (int) -> unicode
		pass
	def getCivicAnarchyLength( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCivicPercentAnger( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCivicUpkeep( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def getCivics( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCivilizationAdjective( self ) :
		# type: () -> str
		""" returns the Civilization name in adjective form """
	def getCivilizationAdjectiveKey( self ) :
		# type: () -> str
		""" returns the Civilization name in adjective form """
	def getCivilizationDescription( self ) :
		# type: () -> str
		""" returns the Civilization Description String """
	def getCivilizationDescriptionKey( self ) :
		# type: () -> str
		""" returns the Civilization Description String """
	def getCivilizationShortDescription( self ) :
		# type: () -> str
		""" returns the short Civilization Description """
	def getCivilizationShortDescriptionKey( self ) :
		# type: () -> str
		""" returns the short Civilization Description """
	def getCivilizationType( self ) :
		# type: () -> int
		pass
	def getCoastalTradeRoutes( self ) :
		# type: () -> int
		pass
	def getCombatExperience( self ) :
		# type: () -> int
		""" Combat experience used to produce Warlords """
	def getCommercePercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCommerceRate( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCommerceRateModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getConscriptCount( self ) :
		# type: () -> int
		pass
	def getConversionTimer( self ) :
		# type: () -> int
		pass
	def getCorporationMaintenanceModifier( self ) :
		# type: () -> int
		pass
	def getCultureHistory( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCurrentEra( self ) :
		# type: () -> int
		pass
	def getCurrentResearch( self ) :
		# type: () -> int
		pass
	def getDistanceMaintenanceModifier( self ) :
		# type: () -> int
		pass
	def getDomesticGreatGeneralRateModifier( self ) :
		# type: () -> int
		pass
	def getEconomyHistory( self, arg0 ) :
		# type: (int) -> int
		pass
	def getEspionageHistory( self, arg0 ) :
		# type: (int) -> int
		pass
	def getEspionageMissionCost( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, CyPlot, int) -> int
		pass
	def getEspionageSpending( self, arg0 ) :
		# type: (int) -> int
		pass
	def getEspionageSpendingWeightAgainstTeam( self, arg0 ) :
		# type: (int) -> int
		pass
	def getEventOccured( self, arg0 ) :
		# type: (int) -> EventTriggeredData
		pass
	def getEventTriggerWeight( self, arg0 ) :
		# type: (int) -> int
		pass
	def getEventTriggered( self, arg0 ) :
		# type: (int) -> EventTriggeredData
		pass
	def getExpInBorderModifier( self ) :
		# type: () -> bool
		pass
	def getExtraBuildingHappiness( self, arg0 ) :
		# type: (int) -> int
		pass
	def getExtraBuildingHealth( self, arg0 ) :
		# type: (int) -> int
		pass
	def getExtraHappiness( self ) :
		# type: () -> int
		pass
	def getExtraHealth( self ) :
		# type: () -> int
		pass
	def getExtraUnitCost( self ) :
		# type: () -> int
		pass
	def getExtraYieldThreshold( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFeatureHappiness( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFeatureProductionModifier( self ) :
		# type: () -> int
		pass
	def getFlagDecal( self ) :
		# type: () -> str
		""" returns the Civilization flag decal """
	def getFreeCityCommerce( self, arg0 ) :
		# type: (int) -> int
		pass
	def getFreeExperience( self ) :
		# type: () -> int
		pass
	def getFreeMilitaryUnitsPopulationPercent( self ) :
		# type: () -> int
		pass
	def getFreeSpecialist( self ) :
		# type: () -> int
		pass
	def getFreeUnitsPopulationPercent( self ) :
		# type: () -> int
		pass
	def getGold( self ) :
		# type: () -> int
		pass
	def getGoldPerMilitaryUnit( self ) :
		# type: () -> int
		pass
	def getGoldPerTurn( self ) :
		# type: () -> int
		pass
	def getGoldPerTurnByPlayer( self, arg0 ) :
		# type: (int) -> int
		pass
	def getGoldPerUnit( self ) :
		# type: () -> int
		pass
	def getGoldenAgeLength( self ) :
		# type: () -> int
		pass
	def getGoldenAgeModifier( self ) :
		# type: () -> int
		pass
	def getGoldenAgeTurns( self ) :
		# type: () -> int
		pass
	def getGreatGeneralRateModifier( self ) :
		# type: () -> int
		pass
	def getGreatGeneralsCreated( self ) :
		# type: () -> int
		pass
	def getGreatGeneralsThresholdModifier( self ) :
		# type: () -> int
		pass
	def getGreatPeopleCreated( self ) :
		# type: () -> int
		pass
	def getGreatPeopleRateModifier( self ) :
		# type: () -> int
		pass
	def getGreatPeopleThresholdModifier( self ) :
		# type: () -> int
		pass
	def getHandicapType( self ) :
		# type: () -> int
		pass
	def getHappyPerMilitaryUnit( self ) :
		# type: () -> int
		pass
	def getHasCorporationCount( self, *args, **kwargs ) :
		pass
	def getHasReligionCount( self, *args, **kwargs ) :
		pass
	def getHighestUnitLevel( self ) :
		# type: () -> int
		pass
	def getHurryCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getHurryModifier( self ) :
		# type: () -> int
		pass
	def getID( self ) :
		# type: () -> int
		pass
	def getImprovementCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getImprovementUpgradeRateModifier( self ) :
		# type: () -> int
		pass
	def getIndustryHistory( self, arg0 ) :
		# type: (int) -> int
		pass
	def getLandScore( self ) :
		# type: () -> int
		pass
	def getLargestCityHappiness( self ) :
		# type: () -> int
		pass
	def getLeaderType( self ) :
		# type: () -> int
		pass
	def getLengthResearchQueue( self ) :
		# type: () -> int
		pass
	def getLevelExperienceModifier( self ) :
		# type: () -> int
		pass
	def getMaxAnarchyTurns( self ) :
		# type: () -> int
		pass
	def getMaxConscript( self ) :
		# type: () -> int
		pass
	def getMaxGlobalBuildingProductionModifier( self ) :
		# type: () -> int
		pass
	def getMaxPlayerBuildingProductionModifier( self ) :
		# type: () -> int
		pass
	def getMaxTeamBuildingProductionModifier( self ) :
		# type: () -> int
		pass
	def getMilitaryProductionModifier( self ) :
		# type: () -> int
		pass
	def getName( self ) :
		# type: () -> str
		pass
	def getNameForm( self ) :
		# type: () -> str
		pass
	def getNameKey( self ) :
		# type: () -> str
		pass
	def getNewCityName( self ) :
		# type: () -> unicode
		pass
	def getNonStateReligionHappiness( self ) :
		# type: () -> int
		pass
	def getNumAvailableBonuses( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNumCities( self ) :
		# type: () -> int
		pass
	def getNumCitiesMaintenanceModifier( self ) :
		# type: () -> int
		pass
	def getNumCityNames( self ) :
		# type: () -> int
		pass
	def getNumGovernmentCenters( self ) :
		# type: () -> int
		pass
	def getNumMilitaryUnits( self ) :
		# type: () -> int
		pass
	def getNumNukeUnits( self ) :
		# type: () -> int
		pass
	def getNumOutsideUnits( self ) :
		# type: () -> int
		pass
	def getNumSelectionGroups( self ) :
		# type: () -> int
		pass
	def getNumTradeBonusImports( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNumTradeableBonuses( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNumUnitGoldenAges( self ) :
		# type: () -> int
		pass
	def getNumUnits( self ) :
		# type: () -> int
		pass
	def getOverflowResearch( self ) :
		# type: () -> int
		pass
	def getPersonalityType( self ) :
		# type: () -> int
		pass
	def getPlayerColor( self ) :
		# type: () -> int
		""" returns the color ID of the player """
	def getPlayerTextColorA( self ) :
		# type: () -> int
		pass
	def getPlayerTextColorB( self ) :
		# type: () -> int
		pass
	def getPlayerTextColorG( self ) :
		# type: () -> int
		pass
	def getPlayerTextColorR( self ) :
		# type: () -> int
		pass
	def getPopScore( self ) :
		# type: () -> int
		pass
	def getPower( self ) :
		# type: () -> int
		pass
	def getPowerHistory( self, arg0 ) :
		# type: (int) -> int
		pass
	def getProjectProductionNeeded( self, arg0, arg1, arg2 ) :
		# type: (int, bool, bool) -> bool
		pass
	def getQueuePosition( self, *args, **kwargs ) :
		""" int """
	def getRealPopulation( self, *args, **kwargs ) :
		""" long int () """
	def getReligionAnarchyLength( self ) :
		# type: () -> int
		pass
	def getResearchTurnsLeft( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def getRevolutionTimer( self ) :
		# type: () -> int
		pass
	def getScoreHistory( self, arg0 ) :
		# type: (int) -> int
		pass
	def getScriptData( self ) :
		# type: () -> str
		""" Get stored custom data (via pickle) """
	def getSeaPlotYield( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSelectionGroup( self, arg0 ) :
		# type: (int) -> CvSelectionGroup
		pass
	def getSingleCivicUpkeep( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def getSpaceProductionModifier( self ) :
		# type: () -> int
		pass
	def getSpecialBuildingNotRequiredCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSpecialistExtraCommerce( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSpecialistExtraYield( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getStartingPlot( self ) :
		# type: () -> CyPlot
		pass
	def getStateReligion( self ) :
		# type: () -> int
		pass
	def getStateReligionBuildingCommerce( self, arg0 ) :
		# type: (int) -> int
		pass
	def getStateReligionBuildingProductionModifier( self ) :
		# type: () -> int
		pass
	def getStateReligionFreeExperience( self ) :
		# type: () -> int
		pass
	def getStateReligionGreatPeopleRateModifier( self ) :
		# type: () -> int
		pass
	def getStateReligionHappiness( self ) :
		# type: () -> int
		pass
	def getStateReligionKey( self ) :
		# type: () -> str
		""" returns the name of the Civilizations State Religion """
	def getStateReligionName( self ) :
		# type: () -> str
		""" returns the name of the Civilizations State Religion """
	def getStateReligionUnitProductionModifier( self ) :
		# type: () -> int
		pass
	def getStrikeTurns( self ) :
		# type: () -> int
		pass
	def getTeam( self ) :
		# type: () -> int
		pass
	def getTechScore( self ) :
		# type: () -> int
		pass
	def getTotalLand( self ) :
		# type: () -> int
		pass
	def getTotalLandScored( self ) :
		# type: () -> int
		pass
	def getTotalMaintenance( self ) :
		# type: () -> int
		pass
	def getTotalPopulation( self ) :
		# type: () -> int
		pass
	def getTotalTimePlayed( self ) :
		# type: () -> int
		pass
	def getTradeDenial( self, arg0, arg1 ) :
		# type: (int, TradeData) -> int
		pass
	def getTradeRoutes( self ) :
		# type: () -> int
		pass
	def getTradeYieldModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnit( self, arg0 ) :
		# type: (int) -> CyUnit
		pass
	def getUnitButton( self, arg0 ) :
		# type: (int) -> str
		""" Returns the unit button for this player """
	def getUnitClassCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitClassCountPlusMaking( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitClassMaking( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitProductionNeeded( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUpkeepCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUpkeepModifier( self ) :
		# type: () -> int
		pass
	def getVotes( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getWarWearinessModifier( self ) :
		# type: () -> int
		pass
	def getWarWearinessPercentAnger( self ) :
		# type: () -> int
		pass
	def getWinsVsBarbs( self ) :
		# type: () -> int
		pass
	def getWondersScore( self ) :
		# type: () -> int
		pass
	def getWorkerSpeedModifier( self ) :
		# type: () -> int
		pass
	def getWorstEnemyName( self ) :
		# type: () -> str
		""" returns the name of the worst enemy """
	def getYieldRateModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def greatPeopleThreshold( self ) :
		# type: () -> int
		pass
	def hasBonus( self, arg0 ) :
		# type: (int) -> int
		pass
	def hasHeadquarters( self, arg0 ) :
		# type: (int) -> bool
		pass
	def hasHolyCity( self, arg0 ) :
		# type: (int) -> bool
		pass
	def hasTrait( self, arg0 ) :
		# type: (int) -> bool
		""" returns True if player is the Trait Type. """
	def initCity( self, plotX, plotY ) :
		# type: (Any, Any) -> Any
		""" spawns a city at x,y """
	def initTriggeredData( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10 ) :
		# type: (int, bool, int, int, int, int, int, int, int, int, int) -> EventTriggeredData
		pass
	def initUnit( self, arg0, plotX, plotY, arg3 ) :
		# type: (int, Any, Any, int) -> CyUnit
		""" place Unit at X,Y   NOTE: Always use UnitAITypes.NO_UNITAI """
	def isAlive( self ) :
		# type: () -> bool
		pass
	def isAnarchy( self ) :
		# type: () -> bool
		pass
	def isBarbarian( self ) :
		# type: () -> bool
		""" returns True if player is a Barbarian """
	def isBuildingClassMaxedOut( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def isBuildingFree( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isBuildingOnlyHealthy( self ) :
		# type: () -> bool
		pass
	def isCivic( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isCommerceFlexible( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isCurrentResearchRepeat( self ) :
		# type: () -> bool
		pass
	def isEverAlive( self ) :
		# type: () -> bool
		pass
	def isExtendedGame( self ) :
		# type: () -> bool
		pass
	def isFeatAccomplished( self ) :
		# type: () -> bool
		pass
	def isFoundedFirstCity( self ) :
		# type: () -> bool
		pass
	def isFullMember( self ) :
		# type: () -> bool
		pass
	def isGoldenAge( self ) :
		# type: () -> bool
		pass
	def isHasCivicOption( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isHuman( self ) :
		# type: () -> bool
		pass
	def isLoyalMember( self ) :
		# type: () -> bool
		pass
	def isMilitaryFoodProduction( self ) :
		# type: () -> bool
		pass
	def isMinorCiv( self ) :
		# type: () -> bool
		pass
	def isNoCivicUpkeep( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isNoCorporations( self ) :
		# type: () -> bool
		pass
	def isNoForeignCorporations( self ) :
		# type: () -> bool
		pass
	def isNoForeignTrade( self ) :
		# type: () -> bool
		pass
	def isNoNonStateReligionSpread( self ) :
		# type: () -> bool
		pass
	def isNoResearchAvailable( self ) :
		# type: () -> bool
		pass
	def isNoUnhealthyPopulation( self ) :
		# type: () -> bool
		pass
	def isNone( self, *args, **kwargs ) :
		""" checks for a null player """
	def isOption( self ) :
		# type: () -> bool
		pass
	def isPlayable( self ) :
		# type: () -> bool
		pass
	def isProductionMaxedBuildingClass( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def isProductionMaxedProject( self, arg0 ) :
		# type: (int) -> int
		pass
	def isProductionMaxedUnitClass( self, arg0 ) :
		# type: (int) -> int
		pass
	def isResearch( self ) :
		# type: () -> bool
		pass
	def isResearchingTech( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isSpecialBuildingNotRequired( self, arg0 ) :
		# type: (int) -> int
		pass
	def isSpecialistValid( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isStateReligion( self ) :
		# type: () -> bool
		pass
	def isStrike( self ) :
		# type: () -> bool
		pass
	def isTurnActive( self ) :
		# type: () -> bool
		pass
	def isUnitClassMaxedOut( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def isVotingMember( self ) :
		# type: () -> bool
		pass
	def isWhiteFlag( self ) :
		# type: () -> bool
		""" Whether or not this player is using a custom texture flag (set in WBS) """
	def killAllDeals( self ) :
		# type: () -> None
		pass
	def killCities( self ) :
		# type: () -> None
		pass
	def killUnits( self ) :
		# type: () -> None
		pass
	def nextCity( self, *args, **kwargs ) :
		""" tuple(CyCity, int iterOut) (int iterIn, bool bReverse) - gets the next city """
	def nextSelectionGroup( self, *args, **kwargs ) :
		""" tuple(CySelectionGroup, int iterOut) (int iterIn, bool bReverse) - gets the next selectionGroup """
	def nextUnit( self, *args, **kwargs ) :
		""" tuple(CyUnit, int iterOut) (int iterIn, bool bReverse) - gets the next unit """
	def popResearch( self, arg0 ) :
		# type: (int) -> None
		pass
	def pushResearch( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def raze( self, arg0 ) :
		# type: (CyCity) -> None
		pass
	def receiveGoody( self, arg0, arg1, arg2 ) :
		# type: (CyPlot, int, CyUnit) -> None
		pass
	def removeBuildingClass( self, arg0 ) :
		# type: (int) -> None
		pass
	def resetEventOccured( self, arg0 ) :
		# type: (int) -> None
		pass
	def revolution( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def setAdvancedStartPoints( self, arg0 ) :
		# type: (int) -> None
		pass
	def setCivics( self, arg0, arg1 ) :
		# type: (int, int) -> None
		""" Used to forcibly set civics with no anarchy """
	def setCombatExperience( self, arg0 ) :
		# type: (int) -> None
		""" Combat experience used to produce Warlords """
	def setCommercePercent( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def setConscriptCount( self, arg0 ) :
		# type: (int) -> None
		pass
	def setCurrentEra( self, arg0 ) :
		# type: (int) -> None
		pass
	def setEspionageSpendingWeightAgainstTeam( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setFeatAccomplished( self ) :
		# type: () -> None
		pass
	def setGold( self, arg0 ) :
		# type: (int) -> None
		pass
	def setLastStateReligion( self, arg0 ) :
		# type: (int) -> None
		""" Sets the player's state religion to iReligionID """
	def setLoyalMember( self ) :
		# type: () -> None
		pass
	def setOption( self ) :
		# type: () -> None
		pass
	def setPersonalityType( self, arg0 ) :
		# type: (int) -> None
		pass
	def setPlayable( self ) :
		# type: () -> None
		pass
	def setScriptData( self, arg0 ) :
		# type: (str) -> None
		""" Set stored custom data (via pickle) """
	def setStartingPlot( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> None
		""" sets the player's starting plot """
	def specialistCommerce( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def specialistYield( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def splitEmpire( self, arg0 ) :
		# type: (int) -> bool
		pass
	def startingPlotRange( self ) :
		# type: () -> int
		pass
	def startingPlotWithinRange( self, arg0, arg1, arg2, arg3 ) :
		# type: (CyPlot, int, int, int) -> bool
		pass
	def stopTradingWithTeam( self, arg0 ) :
		# type: (int) -> int
		pass
	def trigger( self, *args, **kwargs ) :
		""" void (/*EventTriggerTypes*/int eEventTrigger) """
	def unitsGoldenAgeCapable( self ) :
		# type: () -> int
		pass
	def unitsGoldenAgeReady( self ) :
		# type: () -> int
		pass
	def unitsRequiredForGoldenAge( self ) :
		# type: () -> int
		pass

class CyPlot( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def addFeatureDummyModel( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def area( self ) :
		# type: () -> CyArea
		pass
	def at( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def calculateBestNatureYield( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def calculateCulturalOwner( self ) :
		# type: () -> int
		pass
	def calculateCulturePercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def calculateImprovementYieldChange( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, int, bool) -> int
		pass
	def calculateNatureYield( self, arg0, arg1, arg2 ) :
		# type: (int, int, bool) -> int
		pass
	def calculateTeamCulturePercent( self, arg0 ) :
		# type: (int) -> int
		pass
	def calculateTotalBestNatureYield( self, arg0 ) :
		# type: (int) -> int
		pass
	def calculateYield( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def canBuild( self, arg0, arg1, arg2 ) :
		# type: (int, int, bool) -> bool
		pass
	def canHaveBonus( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def canHaveFeature( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canHaveImprovement( self, arg0, arg1, arg2 ) :
		# type: (int, int, bool) -> bool
		pass
	def canHavePotentialIrrigation( self ) :
		# type: () -> bool
		pass
	def changeBuildProgress( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> bool
		pass
	def changeCulture( self, arg0, arg1, arg2 ) :
		# type: (int, int, bool) -> None
		pass
	def changeExtraMovePathCost( self, arg0 ) :
		# type: (int) -> int
		pass
	def changeForceUnownedTimer( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeImprovementDuration( self, arg0 ) :
		# type: (int) -> int
		pass
	def changeInvisibleVisibilityCount( self, *args, **kwargs ) :
		""" int (int (TeamTypes eTeam), int (InvisibleTypes) eInvisible, int iChange) """
	def changeOwnershipDuration( self, arg0 ) :
		# type: (int) -> int
		pass
	def changeUpgradeProgress( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeVisibilityCount( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def countNumAirUnits( self, arg0 ) :
		# type: (int) -> int
		pass
	def countTotalCulture( self ) :
		# type: () -> int
		pass
	def defenseModifier( self, arg0, arg1, arg2 ) :
		# type: (int, bool, bool) -> int
		pass
	def erase( self ) :
		# type: () -> None
		pass
	def findHighestCultureTeam( self ) :
		# type: () -> int
		pass
	def getArea( self ) :
		# type: () -> int
		pass
	def getBestDefender( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (int, int, CvUnit, bool, bool, bool) -> CyUnit
		pass
	def getBonusType( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildProgress( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildTime( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildTurnsLeft( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> int
		pass
	def getCityRadiusCount( self ) :
		# type: () -> int
		pass
	def getCulture( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCultureRangeCities( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getExtraMovePathCost( self ) :
		# type: () -> int
		pass
	def getFeatureProduction( self, arg0, arg1, arg2 ) :
		# type: (int, int, CvCity) -> int
		pass
	def getFeatureType( self ) :
		# type: () -> int
		pass
	def getFeatureVariety( self ) :
		# type: () -> int
		pass
	def getForceUnownedTimer( self ) :
		# type: () -> int
		pass
	def getFoundValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def getImprovementDuration( self ) :
		# type: () -> int
		pass
	def getImprovementType( self ) :
		# type: () -> int
		pass
	def getInvisibleVisibilityCount( self, *args, **kwargs ) :
		""" int (int (TeamTypes eTeam), int (InvisibleTypes) eInvisible) """
	def getLatitude( self ) :
		# type: () -> int
		pass
	def getMinOriginalStartDist( self ) :
		# type: () -> int
		pass
	def getNearestLandArea( self ) :
		# type: () -> int
		pass
	def getNearestLandPlot( self ) :
		# type: () -> CyPlot
		pass
	def getNonObsoleteBonusType( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNumCultureRangeCities( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getNumDefenders( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNumUnits( self ) :
		# type: () -> int
		pass
	def getNumVisibleEnemyDefenders( self, arg0 ) :
		# type: (CyUnit) -> int
		pass
	def getNumVisiblePotentialEnemyDefenders( self, arg0 ) :
		# type: (CyUnit) -> int
		pass
	def getOwner( self ) :
		# type: () -> int
		pass
	def getOwnershipDuration( self ) :
		# type: () -> int
		pass
	def getPlayerCityRadiusCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPlotCity( self ) :
		# type: () -> CyCity
		pass
	def getPlotGroupConnectedBonus( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getPlotType( self ) :
		# type: () -> int
		pass
	def getPoint( self ) :
		# type: () -> NiPoint3
		pass
	def getReconCount( self ) :
		# type: () -> int
		pass
	def getRevealedImprovementType( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def getRevealedOwner( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def getRevealedRouteType( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def getRevealedTeam( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def getRiverCrossingCount( self ) :
		# type: () -> int
		pass
	def getRiverID( self ) :
		# type: () -> int
		pass
	def getRiverNSDirection( self ) :
		# type: () -> int
		pass
	def getRiverWEDirection( self ) :
		# type: () -> int
		pass
	def getRouteType( self ) :
		# type: () -> int
		pass
	def getScriptData( self ) :
		# type: () -> str
		""" Get stored custom data """
	def getSelectedUnit( self ) :
		# type: () -> CyUnit
		pass
	def getStolenVisibilityCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getTeam( self ) :
		# type: () -> int
		pass
	def getTerrainType( self ) :
		# type: () -> int
		pass
	def getUnit( self, arg0 ) :
		# type: (int) -> CyUnit
		pass
	def getUnitPower( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUpgradeProgress( self ) :
		# type: () -> int
		pass
	def getUpgradeTimeLeft( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getVisibilityCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getWorkingCity( self ) :
		# type: () -> CyCity
		pass
	def getWorkingCityOverride( self ) :
		# type: () -> CyCity
		pass
	def getX( self ) :
		# type: () -> int
		pass
	def getY( self ) :
		# type: () -> int
		pass
	def getYield( self, arg0 ) :
		# type: (int) -> int
		pass
	def hasYield( self ) :
		# type: () -> bool
		pass
	def isActiveVisible( self, arg0 ) :
		# type: (bool) -> bool
		pass
	def isAdjacentNonrevealed( self, *args, **kwargs ) :
		pass
	def isAdjacentNonvisible( self, *args, **kwargs ) :
		pass
	def isAdjacentOwned( self ) :
		# type: () -> bool
		pass
	def isAdjacentPlayer( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def isAdjacentPlotGroupConnectedBonus( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def isAdjacentRevealed( self, *args, **kwargs ) :
		pass
	def isAdjacentTeam( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def isAdjacentToArea( self, arg0 ) :
		# type: (CyArea) -> bool
		pass
	def isAdjacentToLand( self ) :
		# type: () -> bool
		pass
	def isAdjacentVisible( self, *args, **kwargs ) :
		pass
	def isBarbarian( self ) :
		# type: () -> bool
		pass
	def isBeingWorked( self ) :
		# type: () -> bool
		pass
	def isBestAdjacentFound( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isBonusNetwork( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isCity( self ) :
		# type: () -> bool
		pass
	def isCityRadius( self ) :
		# type: () -> int
		pass
	def isCoastalLand( self ) :
		# type: () -> bool
		pass
	def isConnectedTo( self, arg0 ) :
		# type: (CvCity) -> bool
		""" returns whether this plot is connected to the provided city """
	def isConnectedToCapital( self, arg0 ) :
		# type: (int) -> bool
		""" returns whether this plot is connected to the capital of the provided player """
	def isCultureRangeCity( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def isEnemyCity( self, arg0 ) :
		# type: (CyUnit) -> bool
		pass
	def isFighting( self ) :
		# type: () -> bool
		pass
	def isFlagDirty( self ) :
		# type: () -> bool
		pass
	def isFlatlands( self ) :
		# type: () -> bool
		pass
	def isForceUnowned( self ) :
		# type: () -> int
		pass
	def isFreshWater( self ) :
		# type: () -> bool
		pass
	def isFriendlyCity( self, arg0, arg1 ) :
		# type: (CyUnit, bool) -> bool
		pass
	def isGoody( self ) :
		# type: () -> bool
		pass
	def isHills( self ) :
		# type: () -> bool
		pass
	def isImpassable( self ) :
		# type: () -> bool
		pass
	def isInvestigate( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isInvisibleVisible( self, *args, **kwargs ) :
		""" int (int (TeamTypes eTeam), int (InvisibleTypes) eInvisible) """
	def isIrrigated( self ) :
		# type: () -> bool
		pass
	def isIrrigationAvailable( self, arg0 ) :
		# type: (bool) -> bool
		pass
	def isLake( self ) :
		# type: () -> bool
		pass
	def isNOfRiver( self ) :
		# type: () -> bool
		pass
	def isNetworkTerrain( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isNone( self ) :
		# type: () -> bool
		pass
	def isOccupation( self ) :
		# type: () -> bool
		pass
	def isOwned( self ) :
		# type: () -> bool
		pass
	def isOwnershipScore( self ) :
		# type: () -> int
		pass
	def isPeak( self ) :
		# type: () -> bool
		pass
	def isPlayerCityRadius( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isPlotGroupConnectedBonus( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def isPotentialCityWork( self ) :
		# type: () -> bool
		pass
	def isPotentialCityWorkForArea( self, arg0 ) :
		# type: (CyArea) -> bool
		pass
	def isPotentialIrrigation( self ) :
		# type: () -> bool
		pass
	def isRevealed( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def isRevealedBarbarian( self ) :
		# type: () -> bool
		pass
	def isRevealedGoody( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isRiver( self ) :
		# type: () -> bool
		pass
	def isRiverConnection( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isRiverCrossing( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isRiverSide( self ) :
		# type: () -> bool
		pass
	def isRoute( self ) :
		# type: () -> bool
		pass
	def isStartingPlot( self ) :
		# type: () -> bool
		pass
	def isTradeNetwork( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isTradeNetworkConnected( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> bool
		pass
	def isTradeNetworkImpassable( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isUnit( self ) :
		# type: () -> bool
		pass
	def isValidDomainForAction( self, arg0 ) :
		# type: (CyUnit) -> bool
		pass
	def isValidDomainForLocation( self, arg0 ) :
		# type: (CyUnit) -> bool
		pass
	def isVisible( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def isVisibleEnemyDefender( self, arg0 ) :
		# type: (CyUnit) -> bool
		pass
	def isVisibleEnemyUnit( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isVisibleOtherUnit( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isVisibleToWatchingHuman( self ) :
		# type: () -> bool
		pass
	def isWOfRiver( self ) :
		# type: () -> bool
		pass
	def isWater( self ) :
		# type: () -> bool
		pass
	def isWithinCultureRange( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isWithinTeamCityRadius( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def movementCost( self, arg0, arg1 ) :
		# type: (CyUnit, CyPlot) -> int
		pass
	def nukeExplosion( self, arg0, arg1 ) :
		# type: (int, CyUnit) -> None
		pass
	def pickFeatureDummyTag( self, arg0, arg1 ) :
		# type: (int, int) -> str
		pass
	def removeGoody( self ) :
		# type: () -> None
		pass
	def resetFeatureModel( self ) :
		# type: () -> None
		pass
	def seeFromLevel( self, arg0 ) :
		# type: (int) -> int
		pass
	def seeThroughLevel( self ) :
		# type: () -> int
		pass
	def setBonusType( self, arg0 ) :
		# type: (int) -> None
		pass
	def setCulture( self, arg0, arg1, arg2 ) :
		# type: (int, int, bool) -> None
		pass
	def setFeatureDummyTexture( self, arg0, arg1 ) :
		# type: (str, str) -> None
		pass
	def setFeatureDummyVisibility( self, arg0, arg1 ) :
		# type: (str, bool) -> None
		pass
	def setFeatureType( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setFlagDirty( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setForceUnownedTimer( self, arg0 ) :
		# type: (int) -> None
		pass
	def setImprovementDuration( self, arg0 ) :
		# type: (int) -> int
		pass
	def setImprovementType( self, arg0 ) :
		# type: (int) -> None
		pass
	def setNOfRiver( self, arg0, arg1 ) :
		# type: (bool, int) -> None
		pass
	def setOwner( self, arg0 ) :
		# type: (int) -> None
		pass
	def setOwnerNoUnitCheck( self, arg0 ) :
		# type: (int) -> None
		pass
	def setOwnershipDuration( self, arg0 ) :
		# type: (int) -> int
		pass
	def setPlotType( self, arg0, arg1, arg2 ) :
		# type: (int, bool, bool) -> None
		pass
	def setRevealed( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, bool, bool, int) -> None
		pass
	def setRiverID( self, arg0 ) :
		# type: (int) -> None
		pass
	def setRouteType( self, arg0 ) :
		# type: (int) -> None
		pass
	def setScriptData( self, arg0 ) :
		# type: (str) -> None
		""" Set stored custom data """
	def setStartingPlot( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setTerrainType( self, arg0, arg1, arg2 ) :
		# type: (int, bool, bool) -> None
		pass
	def setUpgradeProgress( self, arg0 ) :
		# type: (int) -> None
		pass
	def setWOfRiver( self, arg0, arg1 ) :
		# type: (bool, int) -> None
		pass
	def shareAdjacentArea( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def updateVisibility( self, *args, **kwargs ) :
		""" void () Refreshes all of the plots """
	def waterArea( self ) :
		# type: () -> CyArea
		pass

class CyPopup( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def addButton( self, arg0 ) :
		# type: (unicode) -> None
		pass
	def addButtonXY( self, arg0, arg1, arg2 ) :
		# type: (unicode, int, int) -> None
		pass
	def addDDS( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (str, int, int, int, int) -> None
		pass
	def addFixedSeparator( self, arg0 ) :
		# type: (int) -> None
		pass
	def addLeaderhead( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (str, int, int, int, int) -> None
		pass
	def addListBoxString( self, arg0, arg1, arg2 ) :
		# type: (unicode, int, int) -> None
		pass
	def addPullDownString( self, arg0, arg1, arg2 ) :
		# type: (unicode, int, int) -> None
		pass
	def addPythonButton( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6 ) :
		# type: (str, unicode, unicode, str, int, int, bool) -> None
		pass
	def addPythonButtonXY( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8 ) :
		# type: (str, unicode, unicode, str, int, int, bool, int, int) -> None
		pass
	def addPythonDDS( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (str, unicode, int, int, int, int) -> None
		pass
	def addSeparator( self ) :
		# type: () -> None
		pass
	def addTableCellDDS( self, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7 ) :
		# type: (int, int, str, int, int, int, int, int) -> None
		pass
	def addTableCellImage( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, str, int) -> None
		pass
	def addTableCellText( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, int, unicode, int) -> None
		pass
	def completeTableAndAttach( self, arg0 ) :
		# type: (int) -> None
		pass
	def completeTableAndAttachXY( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def createCheckBoxes( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def createEditBox( self, arg0, arg1 ) :
		# type: (unicode, int) -> None
		pass
	def createEditBoxXY( self, arg0, arg1, arg2, arg3 ) :
		# type: (unicode, int, int, int) -> None
		pass
	def createListBox( self, arg0 ) :
		# type: (int) -> None
		pass
	def createListBoxXY( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def createPullDown( self, arg0 ) :
		# type: (int) -> None
		pass
	def createPullDownXY( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def createPythonCheckBoxes( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def createPythonEditBox( self, arg0, arg1, arg2 ) :
		# type: (unicode, unicode, int) -> None
		pass
	def createPythonEditBoxXY( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (unicode, unicode, int, int, int) -> None
		pass
	def createPythonListBox( self, arg0, arg1 ) :
		# type: (unicode, int) -> None
		pass
	def createPythonListBoxXY( self, arg0, arg1, arg2, arg3 ) :
		# type: (unicode, int, int, int) -> None
		pass
	def createPythonPullDown( self, arg0, arg1 ) :
		# type: (unicode, int) -> None
		pass
	def createPythonPullDownXY( self, arg0, arg1, arg2, arg3 ) :
		# type: (unicode, int, int, int) -> None
		pass
	def createPythonRadioButtons( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def createRadioButtons( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def createSpinBox( self, arg0, arg1, arg2, arg3, arg4, arg5 ) :
		# type: (int, unicode, int, int, int, int) -> None
		pass
	def createTable( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def isNone( self ) :
		# type: () -> bool
		""" returns whether this is a valid CyPopup instance """
	def launch( self, *args, **kwargs ) :
		""" bool (bool bCreateOK, PopupStates eState """
	def setBodyString( self, arg0, arg1 ) :
		# type: (unicode, uint) -> None
		pass
	def setCheckBoxText( self, arg0, arg1, arg2 ) :
		# type: (int, unicode, int) -> None
		pass
	def setEditBoxMaxCharCount( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def setHeaderString( self, arg0, arg1 ) :
		# type: (unicode, uint) -> None
		pass
	def setPosition( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setPythonBodyString( self, arg0, arg1, arg2, arg3 ) :
		# type: (unicode, str, unicode, uint) -> None
		pass
	def setPythonCheckBoxText( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, unicode, unicode, int) -> None
		pass
	def setPythonRadioButtonText( self, arg0, arg1, arg2, arg3 ) :
		# type: (int, unicode, unicode, int) -> None
		pass
	def setRadioButtonText( self, arg0, arg1, arg2 ) :
		# type: (int, unicode, int) -> None
		pass
	def setSelectedListBoxString( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setSelectedPulldownID( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setSize( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setTableCellSize( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def setTableYSize( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def setTimer( self, arg0 ) :
		# type: (int) -> None
		pass
	def setUserData( self, arg0 ) :
		# type: (tuple) -> None
		pass

class CyPopupInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def addPopup( self, arg0 ) :
		# type: (int) -> None
		pass
	def addPythonButton( self, arg0, arg1 ) :
		# type: (unicode, str) -> None
		pass
	def getButtonPopupType( self ) :
		# type: () -> int
		pass
	def getData1( self ) :
		# type: () -> int
		pass
	def getData2( self ) :
		# type: () -> int
		pass
	def getData3( self ) :
		# type: () -> int
		pass
	def getFlags( self ) :
		# type: () -> int
		pass
	def getNumPythonButtons( self ) :
		# type: () -> int
		pass
	def getOnClickedPythonCallback( self ) :
		# type: () -> str
		pass
	def getOnFocusPythonCallback( self ) :
		# type: () -> str
		pass
	def getOption1( self ) :
		# type: () -> bool
		pass
	def getOption2( self ) :
		# type: () -> bool
		pass
	def getPythonButtonArt( self ) :
		# type: () -> str
		pass
	def getPythonButtonText( self ) :
		# type: () -> unicode
		pass
	def getPythonModule( self ) :
		# type: () -> str
		pass
	def getText( self ) :
		# type: () -> unicode
		pass
	def isNone( self ) :
		# type: () -> bool
		""" returns whether this is a valid CyPopupInfo instance """
	def setButtonPopupType( self, arg0 ) :
		# type: (int) -> None
		pass
	def setData1( self, arg0 ) :
		# type: (int) -> None
		pass
	def setData2( self, arg0 ) :
		# type: (int) -> None
		pass
	def setData3( self, arg0 ) :
		# type: (int) -> None
		pass
	def setFlags( self, arg0 ) :
		# type: (int) -> None
		pass
	def setOnClickedPythonCallback( self, arg0 ) :
		# type: (str) -> None
		pass
	def setOnFocusPythonCallback( self, arg0 ) :
		# type: (str) -> None
		pass
	def setOption1( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setOption2( self, arg0 ) :
		# type: (bool) -> None
		pass
	def setPythonModule( self, arg0 ) :
		# type: (str) -> None
		pass
	def setText( self, arg0 ) :
		# type: (str) -> None
		pass

class CyPopupReturn( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getButtonClicked( self, arg0 ) :
		# type: (int) -> int
		pass
	def getEditBoxString( self, arg0 ) :
		# type: (int) -> unicode
		pass
	def getSelectedListBoxValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSelectedPullDownValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSelectedRadioButton( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSpinnerWidgetValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def isNone( self ) :
		# type: () -> bool
		""" returns whether this is a valid CyPopupReturn instance """

class CyPythonMgr( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def allowDefaultImpl( self, *args, **kwargs ) :
		pass
	def debugMsg( self, *args, **kwargs ) :
		pass
	def debugMsgWide( self, *args, **kwargs ) :
		pass
	def errorMsg( self, *args, **kwargs ) :
		pass
	def errorMsgWide( self, *args, **kwargs ) :
		pass

class CyRandom( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def get( self, *args, **kwargs ) :
		""" returns a random number """
	def init( self, *args, **kwargs ) :
		""" void (unsigned long int ulSeed) """

class CyReplayInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def createInfo( self ) :
		# type: () -> None
		pass
	def getActivePlayer( self ) :
		# type: () -> int
		pass
	def getCalendar( self ) :
		# type: () -> int
		pass
	def getCivAdjective( self ) :
		# type: () -> unicode
		pass
	def getCivDescription( self ) :
		# type: () -> unicode
		pass
	def getClimate( self ) :
		# type: () -> int
		pass
	def getColor( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDifficulty( self ) :
		# type: () -> int
		pass
	def getEra( self ) :
		# type: () -> int
		pass
	def getFinalAgriculture( self ) :
		# type: () -> int
		pass
	def getFinalDate( self ) :
		# type: () -> unicode
		pass
	def getFinalEconomy( self ) :
		# type: () -> int
		pass
	def getFinalIndustry( self ) :
		# type: () -> int
		pass
	def getFinalScore( self ) :
		# type: () -> int
		pass
	def getFinalTurn( self ) :
		# type: () -> int
		pass
	def getGameSpeed( self ) :
		# type: () -> int
		pass
	def getInitialTurn( self ) :
		# type: () -> int
		pass
	def getLeader( self, arg0 ) :
		# type: (int) -> int
		pass
	def getLeaderName( self ) :
		# type: () -> unicode
		pass
	def getMapHeight( self ) :
		# type: () -> int
		pass
	def getMapScriptName( self ) :
		# type: () -> unicode
		pass
	def getMapWidth( self ) :
		# type: () -> int
		pass
	def getModName( self ) :
		# type: () -> unicode
		pass
	def getNormalizedScore( self ) :
		# type: () -> int
		pass
	def getNumPlayers( self ) :
		# type: () -> int
		pass
	def getNumReplayMessages( self ) :
		# type: () -> int
		pass
	def getPlayerAgriculture( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getPlayerEconomy( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getPlayerIndustry( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getPlayerScore( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getReplayMessageColor( self, arg0 ) :
		# type: (int) -> int
		pass
	def getReplayMessagePlayer( self, arg0 ) :
		# type: (int) -> int
		pass
	def getReplayMessagePlotX( self, arg0 ) :
		# type: (int) -> int
		pass
	def getReplayMessagePlotY( self, arg0 ) :
		# type: (int) -> int
		pass
	def getReplayMessageText( self, arg0 ) :
		# type: (int) -> unicode
		pass
	def getReplayMessageTurn( self, arg0 ) :
		# type: (int) -> int
		pass
	def getReplayMessageType( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSeaLevel( self ) :
		# type: () -> int
		pass
	def getShortCivDescription( self ) :
		# type: () -> unicode
		pass
	def getStartYear( self ) :
		# type: () -> int
		pass
	def getVictoryType( self ) :
		# type: () -> int
		pass
	def getWorldSize( self ) :
		# type: () -> int
		pass
	def isGameOption( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isMultiplayer( self ) :
		# type: () -> bool
		pass
	def isNone( self ) :
		# type: () -> bool
		""" Returns whether or not this is a valid object """
	def isVictoryCondition( self, arg0 ) :
		# type: (int) -> bool
		pass

class CySelectionGroup( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def alwaysInvisible( self ) :
		# type: () -> bool
		pass
	def area( self, *args, **kwargs ) :
		""" CyArea ()* """
	def at( self, iX, iY ) :
		# type: (Any, Any) -> bool
		""" is the group at plot iX, iY? """
	def atPlot( self, arg0 ) :
		# type: (CyPlot) -> bool
		""" is the group at pPlot? """
	def baseMoves( self ) :
		# type: () -> int
		pass
	def canAllMove( self ) :
		# type: () -> bool
		pass
	def canAnyMove( self ) :
		# type: () -> bool
		pass
	def canDefend( self ) :
		# type: () -> bool
		pass
	def canDoCommand( self, *args, **kwargs ) :
		""" bool (eCommand, iData1, iData2, bTestVisible = False) - can the group perform eCommand? """
	def canDoInterfaceMode( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canDoInterfaceModeAt( self, arg0, arg1 ) :
		# type: (int, CyPlot) -> bool
		pass
	def canEnterArea( self, arg0, arg1, arg2 ) :
		# type: (int, CyArea, bool) -> bool
		pass
	def canEnterTerritory( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def canFight( self ) :
		# type: () -> bool
		pass
	def canMoveInto( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		""" can the group move into pPlot? """
	def canMoveOrAttackInto( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		""" can the group move or attack into pPlot? """
	def canMoveThrough( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canStartMission( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, int, int, CyPlot, bool) -> bool
		pass
	def clearMissionQueue( self ) :
		# type: () -> None
		pass
	def countNumUnitAIType( self, *args, **kwargs ) :
		""" int (int (UnitAITypes) eUnitAI """
	def generatePath( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (CyPlot, CyPlot, int, bool, int) -> bool
		pass
	def getActivityType( self ) :
		# type: () -> int
		""" ActivityTypes the group is engaging in """
	def getAutomateType( self ) :
		# type: () -> int
		""" AutomateTypes the group is engaging in """
	def getBestBuildRoute( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> int
		pass
	def getHeadUnit( self ) :
		# type: () -> CyUnit
		pass
	def getID( self ) :
		# type: () -> int
		""" the ID for the SelectionGroup """
	def getLengthMissionQueue( self ) :
		# type: () -> int
		pass
	def getMissionData1( self, arg0 ) :
		# type: (int) -> int
		pass
	def getMissionData2( self, arg0 ) :
		# type: (int) -> int
		pass
	def getMissionFromQueue( self, arg0 ) :
		# type: (int) -> MissionData
		pass
	def getMissionType( self, arg0 ) :
		# type: (int) -> int
		pass
	def getNumUnits( self ) :
		# type: () -> int
		pass
	def getOwner( self ) :
		# type: () -> int
		""" ID for owner of the group """
	def getPathEndTurnPlot( self ) :
		# type: () -> CyPlot
		pass
	def getPathFirstPlot( self ) :
		# type: () -> CyPlot
		pass
	def getTeam( self ) :
		# type: () -> int
		""" ID for team owner of the group """
	def getUnitAt( self, arg0 ) :
		# type: (int) -> CyUnit
		pass
	def hasCargo( self ) :
		# type: () -> bool
		pass
	def hasMoved( self ) :
		# type: () -> bool
		pass
	def hasWorker( self ) :
		# type: () -> bool
		pass
	def isAmphibPlot( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def isAutomated( self ) :
		# type: () -> bool
		""" Is the group automated? """
	def isFull( self ) :
		# type: () -> bool
		pass
	def isHuman( self ) :
		# type: () -> bool
		pass
	def isInvisible( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isNone( self ) :
		# type: () -> bool
		""" is this CySelectionGroup instance valid? """
	def isWaiting( self ) :
		# type: () -> bool
		pass
	def lastMissionPlot( self ) :
		# type: () -> CvPlot
		pass
	def plot( self ) :
		# type: () -> CyPlot
		""" get plot that the group is on """
	def popMission( self ) :
		# type: () -> None
		""" removes mission from queue """
	def pushMission( self, eMission, iData1, iData2, iFlags, bAppend, bManual, eMissionAI, pMissionAIPlot, pMissionAIUnit ) :
		# type: (Any, Any, Any, Any, Any, Any, Any, Any, Any) -> None
		pass
	def pushMoveToMission( self, plotX, plotY ) :
		# type: (Any, Any) -> None
		pass
	def readyToAuto( self ) :
		# type: () -> bool
		pass
	def readyToMove( self, arg0 ) :
		# type: (bool) -> bool
		""" is the group awake and ready to move? """
	def readyToSelect( self, arg0 ) :
		# type: (bool) -> bool
		""" is the group able to be selected? """
	def resetPath( self ) :
		# type: () -> None
		pass
	def setActivityType( self, arg0 ) :
		# type: (int) -> None
		""" set the group to this ActivityTypes """
	def setAutomateType( self, arg0 ) :
		# type: (int) -> None
		""" get the group to perform this AutomateTypes """

class CySign( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getCaption( self ) :
		# type: () -> unicode
		pass
	def getPlayerType( self ) :
		# type: () -> int
		pass
	def getPlot( self ) :
		# type: () -> CyPlot
		pass

class CyStatistics( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getPlayerNumBuildingsBuilt( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getPlayerNumCitiesBuilt( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPlayerNumCitiesRazed( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPlayerNumGoldenAges( self, arg0 ) :
		# type: (int) -> int
		pass
	def getPlayerNumUnitsBuilt( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getPlayerNumUnitsKilled( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getPlayerNumUnitsLost( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getPlayerReligionFounded( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def getPlayerTimePlayed( self, arg0 ) :
		# type: (int) -> int
		""" Returns the amount of time player iPlayerID has played this game for; note that this is only set at the end of the game and will return 0 during a game - use CyGame().getMinutesPlayed() instead """

class CyTeam( object ) :
	def AI_getAtPeaceCounter( self, arg0 ) :
		# type: (int) -> int
		pass
	def AI_getAtWarCounter( self, arg0 ) :
		# type: (int) -> int
		pass
	def AI_getWarSuccess( self, arg0 ) :
		# type: (int) -> int
		pass
	def AI_setWarPlan( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def AI_shareWar( self, arg0 ) :
		# type: (int) -> bool
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	def addTeam( self, arg0 ) :
		# type: (int) -> None
		pass
	def assignVassal( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def canChangeWarPeace( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canContact( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canDeclareWar( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canLaunch( self ) :
		# type: () -> bool
		pass
	def changeBridgeBuildingCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeCommerceFlexibleCount( self, arg0, iChange ) :
		# type: (int, Any) -> None
		pass
	def changeCounterespionageModAgainstTeam( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeCounterespionageTurnsLeftAgainstTeam( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeDefensivePactTradingCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeEnemyWarWearinessModifier( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeEspionagePointsAgainstTeam( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeEspionagePointsEver( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeExtraMoves( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeExtraWaterSeeFromCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeForceTeamVoteEligibilityCount( self, arg0, iChange ) :
		# type: (int, Any) -> None
		pass
	def changeGoldTradingCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeIgnoreIrrigationCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeImprovementYieldChange( self, arg0, arg1, iChange ) :
		# type: (int, int, Any) -> None
		pass
	def changeIrrigationCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeMapTradingCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeNukeInterception( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeOpenBordersTradingCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changePermanentAllianceTradingCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeProjectCount( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeResearchProgress( self, TechID, iChange, iPlayer ) :
		# type: (Any, Any, Any) -> None
		""" edits progress towards TechID """
	def changeRouteChange( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeTechShareCount( self, arg0, iChange ) :
		# type: (int, Any) -> None
		pass
	def changeTechTradingCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeVassalTradingCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def changeWarWeariness( self, arg0, iChange ) :
		# type: (int, Any) -> None
		pass
	def changeWaterWorkCount( self, iChange ) :
		# type: (Any) -> None
		pass
	def countEnemyDangerByArea( self, arg0 ) :
		# type: (CyArea) -> int
		pass
	def countEnemyPowerByArea( self, arg0 ) :
		# type: (CyArea) -> int
		pass
	def countNumAIUnitsByArea( self, arg0, arg1 ) :
		# type: (CyArea, int) -> int
		pass
	def countNumCitiesByArea( self, arg0 ) :
		# type: (CyArea) -> int
		pass
	def countNumUnitsByArea( self, arg0 ) :
		# type: (CyArea) -> int
		pass
	def countPowerByArea( self, arg0 ) :
		# type: (CyArea) -> int
		pass
	def countTotalCulture( self ) :
		# type: () -> int
		pass
	def countTotalPopulationByArea( self, arg0 ) :
		# type: (CyArea) -> int
		pass
	def declareWar( self, arg0, arg1, arg2 ) :
		# type: (int, bool, int) -> None
		""" Forces your team to declare War on iTeam """
	def freeVassal( self, arg0 ) :
		# type: (int) -> None
		pass
	def getAnyWarPlanCount( self, arg0 ) :
		# type: (bool) -> int
		pass
	def getAssets( self ) :
		# type: () -> int
		pass
	def getAtWarCount( self, arg0 ) :
		# type: (bool) -> int
		pass
	def getBridgeBuildingCount( self ) :
		# type: () -> int
		pass
	def getBuildingClassCount( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getBuildingClassCountPlusMaking( self, arg0 ) :
		# type: (int) -> int
		pass
	def getBuildingClassMaking( self, arg0 ) :
		# type: (int) -> int
		pass
	def getChosenWarCount( self, arg0 ) :
		# type: (bool) -> int
		pass
	def getCommerceFlexibleCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCounterespionageModAgainstTeam( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCounterespionageTurnsLeftAgainstTeam( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDefensivePactCount( self ) :
		# type: () -> int
		pass
	def getDefensivePactTradingCount( self ) :
		# type: () -> int
		pass
	def getDefensivePower( self ) :
		# type: () -> int
		pass
	def getEnemyWarWearinessModifier( self ) :
		# type: () -> int
		pass
	def getEspionagePointsAgainstTeam( self, arg0 ) :
		# type: (int) -> int
		pass
	def getEspionagePointsEver( self ) :
		# type: () -> int
		pass
	def getExtraMoves( self, arg0 ) :
		# type: (int) -> int
		pass
	def getExtraWaterSeeFromCount( self ) :
		# type: () -> int
		pass
	def getForceTeamVoteEligibilityCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getGoldTradingCount( self ) :
		# type: () -> int
		pass
	def getHandicapType( self ) :
		# type: () -> int
		pass
	def getHasCorporationCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getHasMetCivCount( self, arg0 ) :
		# type: (bool) -> int
		pass
	def getHasReligionCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getID( self ) :
		# type: () -> int
		""" team ID """
	def getIgnoreIrrigationCount( self ) :
		# type: () -> int
		pass
	def getImprovementYieldChange( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getIrrigationCount( self ) :
		# type: () -> int
		pass
	def getLaunchSuccessRate( self, arg0 ) :
		# type: (int) -> int
		pass
	def getLeaderID( self ) :
		# type: () -> int
		pass
	def getMapTradingCount( self ) :
		# type: () -> int
		pass
	def getMasterPower( self ) :
		# type: () -> int
		pass
	def getName( self ) :
		# type: () -> str
		pass
	def getNukeInterception( self ) :
		# type: () -> int
		pass
	def getNumCities( self, *args, **kwargs ) :
		""" int (); # of cities controlled by team """
	def getNumMembers( self, *args, **kwargs ) :
		""" int (); # of people on team """
	def getNumNukeUnits( self ) :
		# type: () -> int
		pass
	def getObsoleteBuildingCount( self, *args, **kwargs ) :
		pass
	def getOpenBordersTradingCount( self ) :
		# type: () -> int
		pass
	def getPermanentAllianceTradingCount( self ) :
		# type: () -> int
		pass
	def getPower( self, arg0 ) :
		# type: (bool) -> int
		pass
	def getProjectArtType( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def getProjectCount( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getProjectDefaultArtType( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getProjectMaking( self, arg0 ) :
		# type: (int) -> bool
		pass
	def getResearchCost( self, TechID ) :
		# type: (Any) -> int
		""" total cost of Tech """
	def getResearchLeft( self, TechID ) :
		# type: (Any) -> int
		""" Amount of remaining research necessary """
	def getResearchProgress( self, TechID ) :
		# type: (Any) -> int
		""" progress towards finishing research on TechID """
	def getRouteChange( self, RouteType ) :
		# type: (Any) -> int
		""" Route Change caused by RouteType """
	def getSecretaryID( self ) :
		# type: () -> int
		pass
	def getTechCount( self, TechID ) :
		# type: (Any) -> int
		pass
	def getTechShareCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getTechTradingCount( self ) :
		# type: () -> int
		pass
	def getTotalLand( self ) :
		# type: () -> int
		pass
	def getTotalPopulation( self, *args, **kwargs ) :
		""" int (); # of citizens controlled by team """
	def getUnitClassCount( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitClassCountPlusMaking( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitClassMaking( self, arg0 ) :
		# type: (int) -> int
		pass
	def getVassalPower( self ) :
		# type: () -> int
		pass
	def getVassalTradingCount( self ) :
		# type: () -> int
		pass
	def getVictoryCountdown( self, arg0 ) :
		# type: (int) -> int
		pass
	def getVictoryDelay( self, arg0 ) :
		# type: (int) -> int
		pass
	def getWarPlanCount( self, arg0, arg1 ) :
		# type: (int, bool) -> int
		pass
	def getWarWeariness( self, arg0 ) :
		# type: (int) -> int
		pass
	def getWaterWorkCount( self ) :
		# type: () -> int
		pass
	def hasHeadquarters( self, arg0 ) :
		# type: (int) -> bool
		""" does this team have eCorporation's headquarters? """
	def hasHolyCity( self, arg0 ) :
		# type: (int) -> bool
		""" does this team have eReligion's holy city? """
	def hasMetHuman( self ) :
		# type: () -> bool
		pass
	def isAVassal( self ) :
		# type: () -> bool
		pass
	def isAlive( self ) :
		# type: () -> bool
		pass
	def isAtWar( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isBarbarian( self ) :
		# type: () -> bool
		""" is barbarian team? """
	def isBridgeBuilding( self ) :
		# type: () -> bool
		pass
	def isBuildingClassMaxedOut( self, arg0, iExtra ) :
		# type: (int, Any) -> bool
		pass
	def isCommerceFlexible( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isDefensivePact( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isDefensivePactTrading( self ) :
		# type: () -> bool
		pass
	def isEverAlive( self ) :
		# type: () -> bool
		pass
	def isExtraWaterSeeFrom( self ) :
		# type: () -> bool
		pass
	def isForcePeace( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isForceTeamVoteEligible( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isFreeTrade( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isGoldTrading( self ) :
		# type: () -> bool
		""" gold trading? """
	def isHasMet( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isHasTech( self, TechID ) :
		# type: (Any) -> bool
		""" has the team researched techID """
	def isHuman( self ) :
		# type: () -> bool
		""" is human team? """
	def isIgnoreIrrigation( self ) :
		# type: () -> bool
		pass
	def isIrrigation( self ) :
		# type: () -> bool
		pass
	def isMapCentering( self ) :
		# type: () -> bool
		""" map is centered """
	def isMapTrading( self ) :
		# type: () -> bool
		""" map is ready """
	def isMinorCiv( self, *args, **kwargs ) :
		pass
	def isNoTradeTech( self, TechID ) :
		# type: (Any) -> bool
		pass
	def isNone( self ) :
		# type: () -> bool
		""" is this instance valid? """
	def isObsoleteBuilding( self, *args, **kwargs ) :
		""" bool (BuildingID - is BuildingID obsolete? """
	def isOpenBorders( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isOpenBordersTrading( self ) :
		# type: () -> bool
		pass
	def isPermanentAllianceTrading( self ) :
		# type: () -> bool
		pass
	def isPermanentWarPeace( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isProjectAndArtMaxedOut( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isProjectMaxedOut( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def isRiverTrade( self ) :
		# type: () -> bool
		""" will let us know if rivers allow trade """
	def isStolenVisibility( self, arg0 ) :
		# type: (int) -> int
		pass
	def isTechShare( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isTechTrading( self ) :
		# type: () -> bool
		""" tech trading? """
	def isTerrainTrade( self, arg0 ) :
		# type: (int) -> bool
		""" will let us know if this terrain type allows trade """
	def isUnitClassMaxedOut( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def isVassal( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isVassalStateTrading( self ) :
		# type: () -> bool
		pass
	def isWaterWork( self ) :
		# type: () -> bool
		pass
	def makePeace( self, arg0 ) :
		# type: (int) -> None
		""" Forces peace between your team and iTeam """
	def meet( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		""" forces team to meet iTeam """
	def setCounterespionageModAgainstTeam( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setCounterespionageTurnsLeftAgainstTeam( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setEspionagePointsAgainstTeam( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setEspionagePointsEver( self, arg0 ) :
		# type: (int) -> None
		pass
	def setHasTech( self, TechID, bNewValue, iPlayer, bFirst, bAnnounce ) :
		# type: (Any, Any, Any, Any, Any) -> None
		pass
	def setMapCentering( self, bNewValue ) :
		# type: (Any) -> None
		pass
	def setMasterPower( self, arg0 ) :
		# type: (int) -> None
		pass
	def setNoTradeTech( self, TechID, bNewValue ) :
		# type: (Any, Any) -> None
		pass
	def setPermanentWarPeace( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def setProjectArtType( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> None
		pass
	def setProjectDefaultArtType( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setResearchProgress( self, TechID, iNewValue, iPlayer ) :
		# type: (Any, Any, Any) -> None
		""" sets progress towards TechID """
	def setVassal( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def setVassalPower( self, arg0 ) :
		# type: (int) -> None
		pass
	def setWarWeariness( self, arg0, iNewValue ) :
		# type: (int, Any) -> None
		pass
	def signDefensivePact( self, arg0 ) :
		# type: (int) -> None
		pass
	def signOpenBorders( self, arg0 ) :
		# type: (int) -> None
		pass

class CyTranslator( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def changeTextColor( self, arg0, arg1 ) :
		# type: (str, int) -> str
		pass
	def getColorText( self, arg0, arg1, arg2 ) :
		# type: (str, tuple, int) -> str
		pass
	def getObjectText( self, arg0, arg1 ) :
		# type: (str, int) -> str
		pass
	def getText( self, arg0, arg1 ) :
		# type: (str, tuple) -> str
		pass
	def stripHTML( self, arg0 ) :
		# type: (str) -> str
		pass

class CyUnit( object ) :
	def IsSelected( self, *args, **kwargs ) :
		pass
	def NotifyEntity( self, arg0 ) :
		# type: (int) -> None
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	def airBaseCombatStr( self ) :
		# type: () -> int
		pass
	def airBombBaseRate( self ) :
		# type: () -> int
		pass
	def airBombCurrRate( self ) :
		# type: () -> int
		pass
	def airCombatDamage( self, arg0 ) :
		# type: (CyUnit) -> int
		pass
	def airCombatLimit( self ) :
		# type: () -> int
		pass
	def airCurrCombatStr( self, arg0 ) :
		# type: (CyUnit) -> int
		pass
	def airCurrCombatStrFloat( self, arg0 ) :
		# type: (CyUnit) -> float
		pass
	def airMaxCombatStr( self, arg0 ) :
		# type: (CyUnit) -> int
		pass
	def airMaxCombatStrFloat( self, arg0 ) :
		# type: (CyUnit) -> float
		pass
	def airRange( self ) :
		# type: () -> int
		pass
	def alwaysInvisible( self ) :
		# type: () -> bool
		pass
	def animalCombatModifier( self ) :
		# type: () -> int
		pass
	def area( self ) :
		# type: () -> CyArea
		pass
	def at( self, arg0, arg1 ) :
		# type: (int, int) -> bool
		pass
	def atPlot( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def attackForDamage( self, arg0, arg1, arg2 ) :
		# type: (CyUnit, int, int) -> None
		pass
	def attackXPValue( self ) :
		# type: () -> int
		pass
	def baseCombatStr( self ) :
		# type: () -> int
		pass
	def baseMoves( self ) :
		# type: () -> int
		pass
	def bestInterceptor( self, arg0 ) :
		# type: (CyPlot) -> CyUnit
		pass
	def bombardRate( self ) :
		# type: () -> int
		pass
	def bombardTarget( self, arg0 ) :
		# type: (CyPlot) -> CyCity
		pass
	def canAcquirePromotion( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canAcquirePromotionAny( self ) :
		# type: () -> bool
		pass
	def canAirAttack( self ) :
		# type: () -> bool
		pass
	def canAirBomb( self ) :
		# type: () -> bool
		pass
	def canAirBombAt( self, arg0, arg1, arg2 ) :
		# type: (CyPlot, int, int) -> bool
		pass
	def canAirDefend( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canAirPatrol( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canAirlift( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canAirliftAt( self, arg0, arg1, arg2 ) :
		# type: (CyPlot, int, int) -> bool
		pass
	def canAttack( self ) :
		# type: () -> bool
		pass
	def canAutomate( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canBombard( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canBuild( self, arg0, arg1, arg2 ) :
		# type: (CyPlot, int, bool) -> bool
		pass
	def canBuildRoute( self ) :
		# type: () -> bool
		pass
	def canCargoAllMove( self ) :
		# type: () -> bool
		pass
	def canCoexistWithEnemyUnit( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canConstruct( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> bool
		pass
	def canDefend( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canDestroy( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		pass
	def canDiscover( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canDoCommand( self, *args, **kwargs ) :
		""" bool (eCommand, iData1, iData2, bTestVisible = False) - can the unit perform eCommand? """
	def canEnterArea( self, arg0, arg1, arg2 ) :
		# type: (int, CyArea, bool) -> bool
		pass
	def canEnterTerritory( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def canEspionage( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canFight( self ) :
		# type: () -> bool
		pass
	def canFortify( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canFound( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		pass
	def canGift( self, arg0 ) :
		# type: (bool) -> bool
		pass
	def canGiveExperience( self, arg0 ) :
		# type: (CyPlot) -> int
		pass
	def canGoldenAge( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		pass
	def canGreatWork( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canHeal( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canHold( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canHurry( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		pass
	def canInfiltrate( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		pass
	def canJoin( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> bool
		pass
	def canLead( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> int
		pass
	def canLoad( self ) :
		# type: () -> bool
		pass
	def canLoadUnit( self, arg0, arg1 ) :
		# type: (CyUnit, CyPlot) -> bool
		pass
	def canMove( self ) :
		# type: () -> bool
		pass
	def canMoveAllTerrain( self ) :
		# type: () -> bool
		pass
	def canMoveImpassable( self ) :
		# type: () -> bool
		pass
	def canMoveInto( self, arg0, arg1, arg2, arg3 ) :
		# type: (CyPlot, bool, bool, bool) -> bool
		pass
	def canMoveOrAttackInto( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		pass
	def canMoveThrough( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canNuke( self ) :
		# type: () -> bool
		pass
	def canNukeAt( self, arg0, arg1, arg2 ) :
		# type: (CyPlot, int, int) -> bool
		pass
	def canPillage( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canPlunder( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canPromote( self, ePromotion, iLeaderUnitId ) :
		# type: (Any, Any) -> bool
		pass
	def canRecon( self ) :
		# type: () -> bool
		pass
	def canReconAt( self, arg0, arg1, arg2 ) :
		# type: (CyPlot, int, int) -> bool
		pass
	def canSabotage( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		pass
	def canScrap( self ) :
		# type: () -> bool
		pass
	def canSeaPatrol( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canSentry( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canSiege( self, arg0 ) :
		# type: (int) -> bool
		pass
	def canSleep( self, arg0 ) :
		# type: (CyPlot) -> bool
		pass
	def canSpread( self, arg0, arg1, arg2 ) :
		# type: (CyPlot, int, bool) -> bool
		pass
	def canStealPlans( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		pass
	def canTrade( self, arg0, arg1 ) :
		# type: (CyPlot, bool) -> bool
		pass
	def canUnload( self ) :
		# type: () -> bool
		pass
	def canUnloadAll( self ) :
		# type: () -> bool
		pass
	def canUpgrade( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def cargoSpace( self ) :
		# type: () -> int
		pass
	def cargoSpaceAvailable( self ) :
		# type: () -> int
		pass
	def centerCamera( self ) :
		# type: () -> None
		""" Centers the Camera on the unit """
	def chanceFirstStrikes( self ) :
		# type: () -> int
		pass
	def changeCargoSpace( self, arg0 ) :
		# type: (int) -> None
		pass
	def changeDamage( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def changeExperience( self, arg0, arg1, arg2, arg3, arg4 ) :
		# type: (int, int, bool, bool, bool) -> None
		pass
	def changeLevel( self, *args, **kwargs ) :
		pass
	def changeMoves( self, arg0 ) :
		# type: (int) -> None
		pass
	def cityAttackModifier( self ) :
		# type: () -> int
		pass
	def cityDefenseModifier( self ) :
		# type: () -> int
		pass
	def collateralDamage( self ) :
		# type: () -> int
		pass
	def collateralDamageLimit( self ) :
		# type: () -> int
		pass
	def collateralDamageMaxUnits( self ) :
		# type: () -> int
		pass
	def combatLimit( self ) :
		# type: () -> int
		pass
	def convert( self, arg0 ) :
		# type: (CyUnit) -> None
		pass
	def currCombatStr( self, arg0, arg1 ) :
		# type: (CyPlot, CyUnit) -> int
		pass
	def currCombatStrFloat( self, arg0, arg1 ) :
		# type: (CyPlot, CyUnit) -> float
		pass
	def currFirepower( self, arg0, arg1 ) :
		# type: (CyPlot, CyUnit) -> int
		pass
	def currHitPoints( self ) :
		# type: () -> bool
		pass
	def currInterceptionProbability( self ) :
		# type: () -> int
		pass
	def defenseXPValue( self ) :
		# type: () -> int
		pass
	def destroyCost( self, arg0 ) :
		# type: (CyPlot) -> int
		pass
	def destroyProb( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> int
		pass
	def doCommand( self, eCommand, iData1, iData2 ) :
		# type: (Any, Any, Any) -> None
		""" force the unit to perform eCommand """
	def domainCargo( self ) :
		# type: () -> int
		pass
	def domainModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def evasionProbability( self ) :
		# type: () -> int
		pass
	def experienceNeeded( self ) :
		# type: () -> int
		pass
	def featureAttackModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def featureDefenseModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def finishMoves( self ) :
		# type: () -> None
		pass
	def firstStrikes( self ) :
		# type: () -> int
		pass
	def flatMovementCost( self ) :
		# type: () -> bool
		pass
	def flavorValue( self, arg0 ) :
		# type: (int) -> int
		pass
	def fortifyModifier( self ) :
		# type: () -> int
		pass
	def generatePath( self, *args, **kwargs ) :
		""" bool (CyPlot* pToPlot, int iFlags = 0, bool bReuse = false, int* piPathTurns = NULL) """
	def getAdjacentTileHeal( self ) :
		# type: () -> int
		pass
	def getAmphibCount( self ) :
		# type: () -> int
		pass
	def getArtInfo( self, arg0, eEra ) :
		# type: (int, Any) -> CvArtInfoUnit
		pass
	def getBlitzCount( self ) :
		# type: () -> int
		pass
	def getBuildType( self ) :
		# type: () -> int
		pass
	def getButton( self ) :
		# type: () -> str
		pass
	def getCaptureUnitType( self, arg0 ) :
		# type: (int) -> int
		pass
	def getCargo( self ) :
		# type: () -> int
		pass
	def getCivilizationType( self ) :
		# type: () -> int
		pass
	def getCollateralDamageProtection( self ) :
		# type: () -> int
		pass
	def getCombatOwner( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDamage( self ) :
		# type: () -> int
		pass
	def getDeclareWarMove( self, arg0 ) :
		# type: (CyPlot) -> int
		pass
	def getDiscoverResearch( self, arg0 ) :
		# type: (int) -> int
		pass
	def getDiscoveryTech( self ) :
		# type: () -> int
		pass
	def getDomainType( self ) :
		# type: () -> int
		pass
	def getEspionagePoints( self, arg0 ) :
		# type: (CyPlot) -> int
		pass
	def getExperience( self ) :
		# type: () -> int
		pass
	def getExperiencePercent( self ) :
		# type: () -> int
		pass
	def getExtraAirRange( self ) :
		# type: () -> int
		pass
	def getExtraChanceFirstStrikes( self ) :
		# type: () -> int
		pass
	def getExtraCityAttackPercent( self ) :
		# type: () -> int
		pass
	def getExtraCityDefensePercent( self ) :
		# type: () -> int
		pass
	def getExtraCollateralDamage( self ) :
		# type: () -> int
		pass
	def getExtraCombatPercent( self ) :
		# type: () -> int
		pass
	def getExtraDomainModifier( self ) :
		# type: () -> int
		pass
	def getExtraEnemyHeal( self ) :
		# type: () -> int
		pass
	def getExtraEvasion( self ) :
		# type: () -> int
		pass
	def getExtraFeatureAttackPercent( self ) :
		# type: () -> int
		pass
	def getExtraFeatureDefensePercent( self ) :
		# type: () -> int
		pass
	def getExtraFirstStrikes( self ) :
		# type: () -> int
		pass
	def getExtraFriendlyHeal( self ) :
		# type: () -> int
		pass
	def getExtraHillsAttackPercent( self ) :
		# type: () -> int
		pass
	def getExtraHillsDefensePercent( self ) :
		# type: () -> int
		pass
	def getExtraIntercept( self ) :
		# type: () -> int
		pass
	def getExtraMoveDiscount( self ) :
		# type: () -> int
		pass
	def getExtraMoves( self ) :
		# type: () -> int
		pass
	def getExtraNeutralHeal( self ) :
		# type: () -> int
		pass
	def getExtraTerrainAttackPercent( self ) :
		# type: () -> int
		pass
	def getExtraTerrainDefensePercent( self ) :
		# type: () -> int
		pass
	def getExtraUnitCombatModifier( self ) :
		# type: () -> int
		pass
	def getExtraVisibilityRange( self ) :
		# type: () -> int
		pass
	def getExtraWithdrawal( self ) :
		# type: () -> int
		pass
	def getFacingDirection( self ) :
		# type: () -> int
		pass
	def getFortifyTurns( self ) :
		# type: () -> int
		pass
	def getGameTurnCreated( self ) :
		# type: () -> int
		pass
	def getGreatWorkCulture( self, arg0 ) :
		# type: (CyPlot) -> int
		pass
	def getGroup( self ) :
		# type: () -> CySelectionGroup
		pass
	def getGroupID( self ) :
		# type: () -> int
		pass
	def getHandicapType( self ) :
		# type: () -> int
		pass
	def getHotKeyNumber( self ) :
		# type: () -> int
		""" returns the HotKey number for this unit """
	def getHurryProduction( self, arg0 ) :
		# type: (CyPlot) -> int
		pass
	def getID( self ) :
		# type: () -> int
		pass
	def getImmobileTimer( self ) :
		# type: () -> int
		pass
	def getInvisibleType( self ) :
		# type: () -> int
		pass
	def getKamikazePercent( self ) :
		# type: () -> int
		pass
	def getLeaderUnitType( self ) :
		# type: () -> int
		pass
	def getLevel( self ) :
		# type: () -> int
		pass
	def getMaxHurryProduction( self, arg0 ) :
		# type: (CyCity) -> int
		pass
	def getMoves( self ) :
		# type: () -> int
		pass
	def getName( self ) :
		# type: () -> str
		""" Returns the name of a unit along with its type description in parens if using a custom name """
	def getNameForm( self, arg0 ) :
		# type: (int) -> str
		pass
	def getNameKey( self ) :
		# type: () -> str
		pass
	def getNameNoDesc( self ) :
		# type: () -> str
		""" Returns the name of a unit without any description afterwards """
	def getNumSeeInvisibleTypes( self ) :
		# type: () -> int
		pass
	def getOwner( self ) :
		# type: () -> int
		pass
	def getPathEndTurnPlot( self ) :
		# type: () -> CyPlot
		pass
	def getPillageChange( self ) :
		# type: () -> int
		pass
	def getReconPlot( self ) :
		# type: () -> CyPlot
		pass
	def getRevoltProtection( self ) :
		# type: () -> int
		pass
	def getRiverCount( self ) :
		# type: () -> int
		pass
	def getSameTileHeal( self ) :
		# type: () -> int
		pass
	def getScriptData( self ) :
		# type: () -> str
		pass
	def getSeeInvisibleType( self, arg0 ) :
		# type: (int) -> int
		pass
	def getSpecialUnitType( self ) :
		# type: () -> int
		pass
	def getTeam( self ) :
		# type: () -> int
		pass
	def getTradeGold( self, arg0 ) :
		# type: (CyPlot) -> int
		pass
	def getTransportUnit( self ) :
		# type: () -> CyUnit
		pass
	def getUnitAICargo( self, arg0 ) :
		# type: (int) -> int
		pass
	def getUnitAIType( self, *args, **kwargs ) :
		""" int UnitAIType () - returns the int value of the UnitAIType """
	def getUnitClassType( self ) :
		# type: () -> int
		pass
	def getUnitCombatType( self ) :
		# type: () -> int
		pass
	def getUnitType( self ) :
		# type: () -> int
		pass
	def getUpgradeDiscount( self ) :
		# type: () -> int
		pass
	def getVisualOwner( self ) :
		# type: () -> int
		pass
	def getX( self ) :
		# type: () -> int
		pass
	def getY( self ) :
		# type: () -> int
		pass
	def giveExperience( self ) :
		# type: () -> bool
		pass
	def hasCargo( self ) :
		# type: () -> bool
		pass
	def hasMoved( self ) :
		# type: () -> bool
		pass
	def hasUpgrade( self, arg0 ) :
		# type: (bool) -> bool
		pass
	def hillsAttackModifier( self ) :
		# type: () -> int
		pass
	def hillsDefenseModifier( self ) :
		# type: () -> int
		pass
	def ignoreBuildingDefense( self ) :
		# type: () -> bool
		pass
	def ignoreTerrainCost( self ) :
		# type: () -> bool
		pass
	def immuneToFirstStrikes( self ) :
		# type: () -> bool
		pass
	def isActionRecommended( self, arg0 ) :
		# type: (int) -> int
		pass
	def isAlwaysHeal( self ) :
		# type: () -> bool
		pass
	def isAmphib( self ) :
		# type: () -> bool
		pass
	def isAnimal( self ) :
		# type: () -> bool
		pass
	def isAttacking( self ) :
		# type: () -> bool
		pass
	def isAutomated( self ) :
		# type: () -> bool
		pass
	def isBarbarian( self ) :
		# type: () -> bool
		pass
	def isBetterDefenderThan( self, arg0, arg1 ) :
		# type: (CyUnit, CyUnit) -> bool
		pass
	def isBlitz( self ) :
		# type: () -> bool
		pass
	def isCargo( self ) :
		# type: () -> bool
		pass
	def isCombat( self ) :
		# type: () -> bool
		pass
	def isCounterSpy( self ) :
		# type: () -> bool
		pass
	def isDead( self ) :
		# type: () -> bool
		pass
	def isDefending( self ) :
		# type: () -> bool
		pass
	def isEnemyRoute( self ) :
		# type: () -> bool
		pass
	def isFeatureDoubleMove( self, FeatureType ) :
		# type: (Any) -> bool
		pass
	def isFighting( self ) :
		# type: () -> bool
		pass
	def isFortifyable( self ) :
		# type: () -> bool
		pass
	def isFound( self ) :
		# type: () -> bool
		pass
	def isFull( self ) :
		# type: () -> bool
		pass
	def isGoldenAge( self ) :
		# type: () -> bool
		pass
	def isGroupHead( self ) :
		# type: () -> bool
		pass
	def isHasPromotion( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isHillsDoubleMove( self ) :
		# type: () -> bool
		pass
	def isHuman( self ) :
		# type: () -> bool
		pass
	def isHurt( self ) :
		# type: () -> bool
		pass
	def isInGroup( self ) :
		# type: () -> bool
		pass
	def isInvestigate( self ) :
		# type: () -> bool
		pass
	def isInvisible( self, arg0, arg1 ) :
		# type: (int, bool) -> bool
		pass
	def isMadeAttack( self ) :
		# type: () -> bool
		pass
	def isMadeInterception( self ) :
		# type: () -> bool
		pass
	def isMilitaryHappiness( self ) :
		# type: () -> bool
		pass
	def isNeverInvisible( self ) :
		# type: () -> bool
		pass
	def isNoBadGoodies( self ) :
		# type: () -> bool
		pass
	def isNoCapture( self ) :
		# type: () -> bool
		pass
	def isNone( self ) :
		# type: () -> bool
		""" Is this a valid unit instance? """
	def isNukeImmune( self ) :
		# type: () -> bool
		pass
	def isNukeVictim( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> bool
		pass
	def isOnlyDefensive( self ) :
		# type: () -> bool
		pass
	def isPromotionReady( self ) :
		# type: () -> bool
		pass
	def isPromotionValid( self, arg0 ) :
		# type: (int) -> bool
		pass
	def isRanged( self ) :
		# type: () -> bool
		pass
	def isRivalTerritory( self ) :
		# type: () -> bool
		pass
	def isRiver( self ) :
		# type: () -> bool
		pass
	def isTerrainDoubleMove( self, TerrainType ) :
		# type: (Any) -> bool
		pass
	def isWaiting( self ) :
		# type: () -> bool
		pass
	def jumpToNearestValidPlot( self ) :
		# type: () -> bool
		pass
	def kill( self, arg0, arg1 ) :
		# type: (bool, int) -> None
		pass
	def lead( self, arg0 ) :
		# type: (int) -> bool
		pass
	def maxCombatStr( self, arg0, arg1 ) :
		# type: (CyPlot, CyUnit) -> int
		pass
	def maxCombatStrFloat( self, arg0, arg1 ) :
		# type: (CyPlot, CyUnit) -> float
		pass
	def maxFirstStrikes( self ) :
		# type: () -> int
		pass
	def maxHitPoints( self ) :
		# type: () -> bool
		pass
	def maxInterceptionProbability( self ) :
		# type: () -> int
		pass
	def maxMoves( self ) :
		# type: () -> int
		pass
	def maxXPValue( self ) :
		# type: () -> int
		pass
	def movesLeft( self ) :
		# type: () -> int
		pass
	def noDefensiveBonus( self ) :
		# type: () -> bool
		pass
	def nukeRange( self ) :
		# type: () -> int
		pass
	def plot( self ) :
		# type: () -> CyPlot
		pass
	def promote( self, ePromotion ) :
		# type: (Any) -> bool
		pass
	def rangeStrike( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def rotateFacingDirectionClockwise( self ) :
		# type: () -> None
		pass
	def rotateFacingDirectionCounterClockwise( self ) :
		# type: () -> None
		pass
	def sabotageCost( self, arg0 ) :
		# type: (CyPlot) -> int
		pass
	def sabotageProb( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> int
		pass
	def setBaseCombatStr( self, arg0 ) :
		# type: (int) -> None
		pass
	def setDamage( self, arg0, arg1 ) :
		# type: (int, int) -> None
		pass
	def setExperience( self, arg0 ) :
		# type: (int) -> None
		pass
	def setHasPromotion( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		pass
	def setHotKeyNumber( self, arg0 ) :
		# type: (int) -> None
		pass
	def setImmobileTimer( self, arg0 ) :
		# type: (int) -> None
		pass
	def setLeaderUnitType( self, arg0 ) :
		# type: (int) -> None
		pass
	def setLevel( self, *args, **kwargs ) :
		pass
	def setMadeAttack( self, arg0 ) :
		# type: (int) -> None
		pass
	def setMadeInterception( self, arg0 ) :
		# type: (int) -> None
		pass
	def setMoves( self, arg0 ) :
		# type: (int) -> None
		pass
	def setName( self, arg0 ) :
		# type: (str) -> None
		pass
	def setPromotionReady( self, arg0 ) :
		# type: (int) -> None
		pass
	def setReconPlot( self, arg0 ) :
		# type: (CyPlot) -> None
		pass
	def setScriptData( self, arg0 ) :
		# type: (str) -> None
		pass
	def setTransportUnit( self, arg0 ) :
		# type: (CyUnit) -> None
		pass
	def setUnitAIType( self, *args, **kwargs ) :
		""" void UnitAIType (int iUnitAIType) - sets the unit's UnitAIType """
	def setXY( self, arg0, arg1 ) :
		# type: (int, int) -> int
		pass
	def specialCargo( self ) :
		# type: () -> int
		pass
	def stealPlansCost( self, arg0 ) :
		# type: (CyPlot) -> int
		pass
	def stealPlansProb( self, arg0, arg1 ) :
		# type: (CyPlot, int) -> int
		pass
	def terrainAttackModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def terrainDefenseModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def unitClassAttackModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def unitClassDefenseModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def unitCombatModifier( self, arg0 ) :
		# type: (int) -> int
		pass
	def upgradeAvailable( self, arg0, arg1, arg2 ) :
		# type: (int, int, int) -> bool
		pass
	def upgradePrice( self, arg0 ) :
		# type: (int) -> int
		pass
	def visibilityRange( self ) :
		# type: () -> int
		pass
	def withdrawalProbability( self ) :
		# type: () -> int
		pass
	def workRate( self, arg0 ) :
		# type: (bool) -> int
		pass

class CyUnitEntity( object ) :
	def GetSubEntity( self, uint ) :
		# type: (Any) -> CyUnitSubEnitty
		""" Returns the CySubUnitEntity at the given index """
	def GetSubEntityCount( self ) :
		# type: () -> uint
		""" Returns the number of CyUnitSubEntitys in this unit """
	def GetUnitsCurrentlyAlive( self ) :
		# type: () -> int
		""" Returns the number of sub-units that are alive """
	def MoveTo( self, x, y, z, rad ) :
		# type: (Any, Any, Any, Any) -> None
		""" Moves the unit to the given position """
	def NotifyEntity( self, arg0 ) :
		# type: (int) -> None
		""" Notifies this entity of the given event """
	def __init__( self, *args, **kwargs ) :
		pass
	def getScale( self ) :
		# type: () -> float
		pass
	def getUnit( self ) :
		# type: () -> CyUnit
		""" Returns the CyUnit associated with this CyUnitEntity """
	def isNone( self ) :
		# type: () -> bool
		""" Is this instance valid? """
	def setScale( self, arg0 ) :
		# type: (float) -> None
		pass

class CyUnitSubEntity( object ) :
	def PlayAnimationPath( self, arg0 ) :
		# type: (int) -> None
		""" Plays the given animation path """
	def __init__( self, *args, **kwargs ) :
		pass
	def isNone( self ) :
		# type: () -> bool
		""" Is this instance valid? """
	def setUnitShadow( self, arg0 ) :
		# type: (bool) -> None
		""" shows/hides a sub-unit's shadow """
	def setVisible( self, arg0 ) :
		# type: (bool) -> None
		""" shows/hides a sub-unit """

class CyUserProfile( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def deleteProfileFile( self, arg0 ) :
		# type: (str) -> bool
		""" Deletes the file (no extension) in Civ4\Profiles\ IF it exists - returns whether or not a file actually was deleted """
	def getAmbienceVolume( self ) :
		# type: () -> int
		""" returns the Ambiance volume level """
	def getAntiAliasing( self ) :
		# type: () -> int
		""" returns the number of Anti-Aliasing MultiSamples level currently enabled """
	def getAntiAliasingMaxMultiSamples( self ) :
		# type: () -> int
		""" return the number of Anti-Aliasing MultiSamples available on the video card """
	def getCaptureDeviceDesc( self, arg0 ) :
		# type: (int) -> str
		""" returns name of capture device at provided index """
	def getCaptureDeviceIndex( self ) :
		# type: () -> int
		""" returns the index of currently selected capture device """
	def getCaptureVolume( self ) :
		# type: () -> int
		""" returns current capture volume """
	def getCurrentVersion( self ) :
		# type: () -> int
		""" Returns the current version of the user profile system in place """
	def getGlobeLayer( self ) :
		# type: () -> int
		pass
	def getGlobeViewRenderLevel( self ) :
		# type: () -> int
		""" returns the globe view render level """
	def getGraphicOption( self, arg0 ) :
		# type: (int) -> bool
		""" returns value of option i """
	def getGraphicsLevel( self ) :
		# type: () -> int
		""" returns the graphics quality level """
	def getGrid( self ) :
		# type: () -> bool
		pass
	def getInterfaceVolume( self ) :
		# type: () -> int
		""" returns the Interface volume level """
	def getMainMenu( self ) :
		# type: () -> int
		""" returns the main menu index currently used """
	def getMap( self ) :
		# type: () -> bool
		pass
	def getMasterVolume( self ) :
		# type: () -> int
		""" returns the Master volume level """
	def getMaxCaptureVolume( self ) :
		# type: () -> int
		""" returns max range of capture volume """
	def getMaxPlaybackVolume( self ) :
		# type: () -> int
		""" returns max range of Playback volume """
	def getMovieQualityLevel( self ) :
		# type: () -> int
		""" returns the movie quality level """
	def getMusicPath( self ) :
		# type: () -> str
		""" Returns the current custom music folder path (blank if no path set) """
	def getMusicVolume( self ) :
		# type: () -> int
		""" returns the music volume level """
	def getNumCaptureDevices( self ) :
		# type: () -> int
		""" returns number of available voice capture devices """
	def getNumPlaybackDevices( self ) :
		# type: () -> int
		""" returns number of available voice Playback devices """
	def getNumProfileFiles( self ) :
		# type: () -> uint
		""" Returns the number of .prf files in the the Civ4\Profiles\ directory """
	def getPlaybackDeviceDesc( self, arg0 ) :
		# type: (int) -> str
		""" returns name of Playback device at provided index """
	def getPlaybackDeviceIndex( self ) :
		# type: () -> int
		""" returns the index of currently selected Playback device """
	def getPlaybackVolume( self ) :
		# type: () -> int
		""" returns current Playback volume """
	def getPlayerOption( self, arg0 ) :
		# type: (int) -> bool
		""" returns value of option i """
	def getProfileFileName( self, arg0 ) :
		# type: (int) -> str
		""" Returns the name of the file associated with iFileID """
	def getProfileName( self ) :
		# type: () -> str
		""" Returns the name of the current profile """
	def getProfileVersion( self ) :
		# type: () -> int
		""" Returns the version number of the active profile """
	def getRenderQualityLevel( self ) :
		# type: () -> int
		""" returns the render Quality level """
	def getResolution( self ) :
		# type: () -> int
		""" returns the Resolution option currently enabled """
	def getResolutionMaxModes( self ) :
		# type: () -> int
		""" returns the number of supported resolutions """
	def getResolutionString( self, arg0 ) :
		# type: (int) -> str
		""" returns the resolution string for the associated resolution index """
	def getScores( self ) :
		# type: () -> bool
		pass
	def getSoundEffectsVolume( self ) :
		# type: () -> int
		""" returns the sound effects volume level """
	def getSpeakerConfig( self ) :
		# type: () -> str
		""" returns the name of the currently active Speaker Configuration """
	def getSpeakerConfigFromList( self, arg0 ) :
		# type: (int) -> str
		""" returns the speaker configuration associated with iIndex """
	def getSpeechVolume( self ) :
		# type: () -> int
		""" returns the Speech volume level """
	def getVolumeStops( self ) :
		# type: () -> int
		""" returns the number of stops that should be available for each volume slider """
	def getYields( self ) :
		# type: () -> bool
		pass
	def is24Hours( self ) :
		# type: () -> bool
		""" is the 24 hour system enabled? """
	def isAmbienceNoSound( self ) :
		# type: () -> bool
		""" returns whether or not Ambiance sound is disabled """
	def isClockOn( self ) :
		# type: () -> bool
		""" is the clock on? """
	def isInterfaceNoSound( self ) :
		# type: () -> bool
		""" returns whether or not Interface sound is disabled """
	def isMasterNoSound( self ) :
		# type: () -> bool
		""" returns whether or not Master sound is disabled """
	def isMusicNoSound( self ) :
		# type: () -> bool
		""" returns whether or not Music sound is disabled """
	def isProfileFileExist( self, arg0 ) :
		# type: (str) -> bool
		""" Returns whether or not szFileName (no extension) exists in Civ4\Profiles\ """
	def isSoundEffectsNoSound( self ) :
		# type: () -> bool
		""" returns whether or not SoundEffects sound is disabled """
	def isSpeechNoSound( self ) :
		# type: () -> bool
		""" returns whether or not Speech sound is disabled """
	def loadProfileFileNames( self, *args, **kwargs ) :
		""" void - Recalculates the list of Profile files that exist """
	def musicPathDialogBox( self ) :
		# type: () -> None
		""" Brings up a dialog box which is used to allow the user to set a custom music directory) """
	def readFromFile( self, arg0 ) :
		# type: (str) -> bool
		""" Reads the CvUserProfile data from file szFileName; returns whether or not the read was successful """
	def recalculateAudioSettings( self ) :
		# type: () -> None
		""" enacts audio setting members to the audio system """
	def resetOptions( self, arg0 ) :
		# type: (int) -> None
		""" Resets the options to default (Tabgroup type - use NOTABGROUP to reset all user profile data """
	def set24Hours( self, arg0 ) :
		# type: (bool) -> None
		""" set the 24 hour system to state bValue """
	def setAmbienceNoSound( self, arg0 ) :
		# type: (bool) -> None
		""" sets whether or not Ambiance sound is disabled """
	def setAmbienceVolume( self, arg0 ) :
		# type: (int) -> None
		""" sets the Ambiance volume to i """
	def setAntiAliasing( self, arg0 ) :
		# type: (int) -> None
		""" sets the Anti-Aliasing MultiSamples level currently enabled to i """
	def setCaptureDevice( self, arg0 ) :
		# type: (int) -> None
		""" selects a capture device """
	def setCaptureVolume( self, arg0 ) :
		# type: (int) -> None
		""" sets capture volume """
	def setClockJustTurnedOn( self, arg0 ) :
		# type: (bool) -> None
		""" set clock just turned on to state bValue """
	def setClockOn( self, arg0 ) :
		# type: (bool) -> None
		""" set the clock to state bValue """
	def setGlobeViewRenderLevel( self, arg0 ) :
		# type: (int) -> None
		""" sets the globe view render level """
	def setGraphicOption( self, arg0, arg1 ) :
		# type: (int, bool) -> None
		""" sets the value of option i to b """
	def setGraphicsLevel( self, arg0 ) :
		# type: (int) -> None
		""" sets the Graphics quality to i """
	def setInterfaceNoSound( self, arg0 ) :
		# type: (bool) -> None
		""" sets whether or not Interface sound is disabled """
	def setInterfaceVolume( self, arg0 ) :
		# type: (int) -> None
		""" sets the Interface volume to i """
	def setMainMenu( self, arg0 ) :
		# type: (int) -> None
		""" sets the main menu index currently used """
	def setMasterNoSound( self, arg0 ) :
		# type: (bool) -> None
		""" sets whether or not Master sound is disabled """
	def setMasterVolume( self, arg0 ) :
		# type: (int) -> None
		""" sets the Master volume to i """
	def setMovieQualityLevel( self, arg0 ) :
		# type: (int) -> None
		""" sets the movie quality level """
	def setMusicNoSound( self, arg0 ) :
		# type: (bool) -> None
		""" sets whether or not Music sound is disabled """
	def setMusicPath( self, arg0 ) :
		# type: (str) -> None
		""" sets the custom music folder path """
	def setMusicVolume( self, arg0 ) :
		# type: (int) -> None
		""" sets the music volume to i """
	def setPlaybackDevice( self, arg0 ) :
		# type: (int) -> None
		""" selects a Playback device """
	def setPlaybackVolume( self, arg0 ) :
		# type: (int) -> None
		""" sets Playback volume """
	def setProfileName( self, arg0 ) :
		# type: (str) -> None
		""" Assigns the internal UserProfile name to szNewName """
	def setRenderQualityLevel( self, arg0 ) :
		# type: (int) -> None
		""" sets the render Quality level """
	def setResolution( self, arg0 ) :
		# type: (int) -> bool
		""" sets the Resolution option currently enabled to i """
	def setSoundEffectsNoSound( self, arg0 ) :
		# type: (bool) -> None
		""" sets whether or not SoundEffects sound is disabled """
	def setSoundEffectsVolume( self, arg0 ) :
		# type: (int) -> None
		""" sets the sound effects volume to i """
	def setSpeakerConfig( self, arg0 ) :
		# type: (str) -> None
		""" sets the Speaker Configuration to szConfigName if it is a valid choice """
	def setSpeechNoSound( self, arg0 ) :
		# type: (bool) -> None
		""" sets whether or not Speech sound is disabled """
	def setSpeechVolume( self, arg0 ) :
		# type: (int) -> None
		""" sets the Speech volume to i """
	def setUseVoice( self, arg0 ) :
		# type: (bool) -> None
		""" sets whether to use voice capture/playback """
	def useVoice( self ) :
		# type: () -> bool
		""" returns whether or not to use voice capture/playback """
	def wasClockJustTurnedOn( self ) :
		# type: () -> bool
		""" was the clock just turned on? """
	def writeToFile( self, arg0 ) :
		# type: (str) -> None
		""" Writes the CvUserProfile data to file szFileName """

class CyVariableSystem( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getFirstVariableName( self ) :
		# type: () -> str
		pass
	def getNextVariableName( self ) :
		# type: () -> str
		pass
	def getValueFloat( self, arg0 ) :
		# type: (str) -> float
		pass
	def getValueInt( self, arg0 ) :
		# type: (str) -> int
		pass
	def getValueString( self, arg0 ) :
		# type: (str) -> str
		pass
	def getVariableType( self, arg0 ) :
		# type: (str) -> str
		pass
	def isNone( self ) :
		# type: () -> bool
		""" Is this instance valid? """
	def setValueFloat( self, arg0, arg1 ) :
		# type: (str, float) -> Any
		pass
	def setValueInt( self, arg0, arg1 ) :
		# type: (str, int) -> Any
		pass
	def setValueString( self, arg0, arg1 ) :
		# type: (str, str) -> Any
		pass

def DLLProfilerCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class DenialTypes :
	DENIAL_ANGER_CIVIC = 5 # type: DenialTypes
	DENIAL_ATTITUDE = 10 # type: DenialTypes
	DENIAL_ATTITUDE_THEM = 11 # type: DenialTypes
	DENIAL_CONTACT_THEM = 8 # type: DenialTypes
	DENIAL_FAVORITE_CIVIC = 6 # type: DenialTypes
	DENIAL_JOKING = 4 # type: DenialTypes
	DENIAL_MINORITY_RELIGION = 7 # type: DenialTypes
	DENIAL_MYSTERY = 3 # type: DenialTypes
	DENIAL_NEVER = 1 # type: DenialTypes
	DENIAL_NOT_ALLIED = 19 # type: DenialTypes
	DENIAL_NO_GAIN = 18 # type: DenialTypes
	DENIAL_POWER_THEM = 16 # type: DenialTypes
	DENIAL_POWER_US = 14 # type: DenialTypes
	DENIAL_POWER_YOU = 15 # type: DenialTypes
	DENIAL_POWER_YOUR_ENEMIES = 22 # type: DenialTypes
	DENIAL_RECENT_CANCEL = 20 # type: DenialTypes
	DENIAL_TECH_MONOPOLY = 13 # type: DenialTypes
	DENIAL_TECH_WHORE = 12 # type: DenialTypes
	DENIAL_TOO_FAR = 23 # type: DenialTypes
	DENIAL_TOO_MANY_WARS = 17 # type: DenialTypes
	DENIAL_TOO_MUCH = 2 # type: DenialTypes
	DENIAL_UNKNOWN = 0 # type: DenialTypes
	DENIAL_VICTORY = 9 # type: DenialTypes
	DENIAL_WORST_ENEMY = 21 # type: DenialTypes
	NO_DENIAL = -1 # type: DenialTypes

class DiploCommentTypes :
	NO_DIPLOCOMMENT = -1 # type: DiploCommentTypes

class DiploEventTypes :
	DIPLOEVENT_ACCEPT_DEMAND = 5 # type: DiploEventTypes
	DIPLOEVENT_AI_CONTACT = 1 # type: DiploEventTypes
	DIPLOEVENT_ASK_HELP = 16 # type: DiploEventTypes
	DIPLOEVENT_CONTACT = 0 # type: DiploEventTypes
	DIPLOEVENT_CONVERT = 8 # type: DiploEventTypes
	DIPLOEVENT_DEMAND_WAR = 7 # type: DiploEventTypes
	DIPLOEVENT_FAILED_CONTACT = 2 # type: DiploEventTypes
	DIPLOEVENT_GIVE_HELP = 3 # type: DiploEventTypes
	DIPLOEVENT_JOIN_WAR = 12 # type: DiploEventTypes
	DIPLOEVENT_MADE_DEMAND = 17 # type: DiploEventTypes
	DIPLOEVENT_MADE_DEMAND_VASSAL = 20 # type: DiploEventTypes
	DIPLOEVENT_NO_CONVERT = 9 # type: DiploEventTypes
	DIPLOEVENT_NO_JOIN_WAR = 13 # type: DiploEventTypes
	DIPLOEVENT_NO_REVOLUTION = 11 # type: DiploEventTypes
	DIPLOEVENT_NO_STOP_TRADING = 15 # type: DiploEventTypes
	DIPLOEVENT_REFUSED_HELP = 4 # type: DiploEventTypes
	DIPLOEVENT_REJECTED_DEMAND = 6 # type: DiploEventTypes
	DIPLOEVENT_RESEARCH_TECH = 18 # type: DiploEventTypes
	DIPLOEVENT_REVOLUTION = 10 # type: DiploEventTypes
	DIPLOEVENT_STOP_TRADING = 14 # type: DiploEventTypes
	DIPLOEVENT_TARGET_CITY = 19 # type: DiploEventTypes
	NO_DIPLOEVENT = -1 # type: DiploEventTypes
	NUM_DIPLOEVENT_TYPES = 21 # type: DiploEventTypes

class DiplomacyPowerTypes :
	DIPLOMACYPOWER_EQUAL = 1 # type: DiplomacyPowerTypes
	DIPLOMACYPOWER_STRONGER = 2 # type: DiplomacyPowerTypes
	DIPLOMACYPOWER_WEAKER = 0 # type: DiplomacyPowerTypes
	NO_DIPLOMACYPOWER = -1 # type: DiplomacyPowerTypes
	NUM_DIPLOMACYPOWER_TYPES = 3 # type: DiplomacyPowerTypes

def Direct3DQueryCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class DirectionTypes :
	DIRECTION_EAST = 2 # type: DirectionTypes
	DIRECTION_NORTH = 0 # type: DirectionTypes
	DIRECTION_NORTHEAST = 1 # type: DirectionTypes
	DIRECTION_NORTHWEST = 7 # type: DirectionTypes
	DIRECTION_SOUTH = 4 # type: DirectionTypes
	DIRECTION_SOUTHEAST = 3 # type: DirectionTypes
	DIRECTION_SOUTHWEST = 5 # type: DirectionTypes
	DIRECTION_WEST = 6 # type: DirectionTypes
	NO_DIRECTION = -1 # type: DirectionTypes
	NUM_DIRECTION_TYPES = 8 # type: DirectionTypes

def DisableTextureCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def DisplayCutTreesCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def DisplayQuadTreeCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class DomainTypes :
	DOMAIN_AIR = 1 # type: DomainTypes
	DOMAIN_IMMOBILE = 3 # type: DomainTypes
	DOMAIN_LAND = 2 # type: DomainTypes
	DOMAIN_SEA = 0 # type: DomainTypes
	NUM_DOMAIN_TYPES = 4 # type: DomainTypes

def DumpGeoStatsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class EmphasizeTypes :
	NO_EMPHASIZE = -1 # type: EmphasizeTypes

class EndTurnButtonStates :
	END_TURN_GO = 0 # type: EndTurnButtonStates
	END_TURN_OVER_DARK = 2 # type: EndTurnButtonStates
	END_TURN_OVER_HIGHLIGHT = 1 # type: EndTurnButtonStates
	NUM_END_TURN_STATES = 3 # type: EndTurnButtonStates

class EngineDirtyBits :
	CultureBorders_DIRTY_BIT = 3 # type: EngineDirtyBits
	GlobeTexture_DIRTY_BIT = 0 # type: EngineDirtyBits
	MinimapTexture_DIRTY_BIT = 2 # type: EngineDirtyBits
	NUM_ENGINE_DIRTY_BITS = 4 # type: EngineDirtyBits

class EntityEventTypes :
	ENTITY_EVENT_NONE = -1 # type: EntityEventTypes

class EraTypes :
	NO_ERA = -1 # type: EraTypes

class EspionageMissionTypes :
	NO_ESPIONAGEMISSION = -1 # type: EspionageMissionTypes

class EventContextTypes :
	EVENTCONTEXT_ALL = 1 # type: EventContextTypes
	EVENTCONTEXT_SELF = 0 # type: EventContextTypes
	NO_EVENTCONTEXT = -1 # type: EventContextTypes

class EventMessage( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getDescription( self, *args, **kwargs ) :
		pass
	@property
	def iExpirationTurn( self ) :
		# type: () -> Any
		pass
	@iExpirationTurn.setter
	def iExpirationTurn( self, value ) :
		# type: (Any) -> None
		pass

class EventTriggerTypes :
	NO_EVENTTRIGGER = -1 # type: EventTriggerTypes

class EventTriggeredData( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def eBuilding( self ) :
		# type: () -> Any
		pass
	@eBuilding.setter
	def eBuilding( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def eCorporation( self ) :
		# type: () -> Any
		pass
	@eCorporation.setter
	def eCorporation( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def eOtherPlayer( self ) :
		# type: () -> Any
		pass
	@eOtherPlayer.setter
	def eOtherPlayer( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def ePlayer( self ) :
		# type: () -> Any
		pass
	@ePlayer.setter
	def ePlayer( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def eReligion( self ) :
		# type: () -> Any
		pass
	@eReligion.setter
	def eReligion( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def eTrigger( self ) :
		# type: () -> Any
		pass
	@eTrigger.setter
	def eTrigger( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iCityId( self ) :
		# type: () -> Any
		pass
	@iCityId.setter
	def iCityId( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iId( self ) :
		# type: () -> Any
		pass
	@iId.setter
	def iId( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iOtherPlayerCityId( self ) :
		# type: () -> Any
		pass
	@iOtherPlayerCityId.setter
	def iOtherPlayerCityId( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iPlotX( self ) :
		# type: () -> Any
		pass
	@iPlotX.setter
	def iPlotX( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iPlotY( self ) :
		# type: () -> Any
		pass
	@iPlotY.setter
	def iPlotY( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iTurn( self ) :
		# type: () -> Any
		pass
	@iTurn.setter
	def iTurn( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iUnitId( self ) :
		# type: () -> Any
		pass
	@iUnitId.setter
	def iUnitId( self, value ) :
		# type: (Any) -> None
		pass

class EventType :
	EVT_BACK = 4 # type: EventType
	EVT_FORWARD = 5 # type: EventType
	EVT_KEYDOWN = 6 # type: EventType
	EVT_KEYUP = 7 # type: EventType
	EVT_LBUTTONDBLCLICK = 2 # type: EventType
	EVT_LBUTTONDOWN = 1 # type: EventType
	EVT_RBUTTONDOWN = 3 # type: EventType

class EventTypes :
	NO_EVENT = -1 # type: EventTypes

class FOWVis( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getOffsets( self, *args, **kwargs ) :
		pass
	@property
	def uiCount( self ) :
		# type: () -> Any
		pass
	@uiCount.setter
	def uiCount( self, value ) :
		# type: (Any) -> None
		pass

class FeatTypes :
	FEAT_COPPER_CONNECTED = 12 # type: FeatTypes
	FEAT_CORPORATION_ENABLED = 29 # type: FeatTypes
	FEAT_FOOD_CONNECTED = 16 # type: FeatTypes
	FEAT_HORSE_CONNECTED = 13 # type: FeatTypes
	FEAT_IRON_CONNECTED = 14 # type: FeatTypes
	FEAT_LUXURY_CONNECTED = 15 # type: FeatTypes
	FEAT_NATIONAL_WONDER = 10 # type: FeatTypes
	FEAT_PAD = 30 # type: FeatTypes
	FEAT_POPULATION_100_MILLION = 24 # type: FeatTypes
	FEAT_POPULATION_10_MILLION = 21 # type: FeatTypes
	FEAT_POPULATION_1_BILLION = 27 # type: FeatTypes
	FEAT_POPULATION_1_MILLION = 18 # type: FeatTypes
	FEAT_POPULATION_200_MILLION = 25 # type: FeatTypes
	FEAT_POPULATION_20_MILLION = 22 # type: FeatTypes
	FEAT_POPULATION_2_BILLION = 28 # type: FeatTypes
	FEAT_POPULATION_2_MILLION = 19 # type: FeatTypes
	FEAT_POPULATION_500_MILLION = 26 # type: FeatTypes
	FEAT_POPULATION_50_MILLION = 23 # type: FeatTypes
	FEAT_POPULATION_5_MILLION = 20 # type: FeatTypes
	FEAT_POPULATION_HALF_MILLION = 17 # type: FeatTypes
	FEAT_TRADE_ROUTE = 11 # type: FeatTypes
	FEAT_UNITCOMBAT_ARCHER = 0 # type: FeatTypes
	FEAT_UNITCOMBAT_ARMOR = 5 # type: FeatTypes
	FEAT_UNITCOMBAT_GUN = 4 # type: FeatTypes
	FEAT_UNITCOMBAT_HELICOPTER = 6 # type: FeatTypes
	FEAT_UNITCOMBAT_MELEE = 2 # type: FeatTypes
	FEAT_UNITCOMBAT_MOUNTED = 1 # type: FeatTypes
	FEAT_UNITCOMBAT_NAVAL = 7 # type: FeatTypes
	FEAT_UNITCOMBAT_SIEGE = 3 # type: FeatTypes
	FEAT_UNIT_PRIVATEER = 8 # type: FeatTypes
	FEAT_UNIT_SPY = 9 # type: FeatTypes
	NUM_FEAT_TYPES = 31 # type: FeatTypes

class FeatureTypes :
	NO_FEATURE = -1 # type: FeatureTypes

class FlavorTypes :
	NO_FLAVOR = -1 # type: FlavorTypes

class FogOfWarModeTypes :
	FOGOFWARMODE_OFF = 0 # type: FogOfWarModeTypes
	FOGOFWARMODE_UNEXPLORED = 1 # type: FogOfWarModeTypes
	NUM_FOGOFWARMODE_TYPES = 3 # type: FogOfWarModeTypes

def FogofWarCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class FontSymbols :
	ANGRY_POP_CHAR = 17 # type: FontSymbols
	BAD_FOOD_CHAR = 14 # type: FontSymbols
	BAD_GOLD_CHAR = 13 # type: FontSymbols
	BULLET_CHAR = 4 # type: FontSymbols
	DEFENSE_CHAR = 11 # type: FontSymbols
	DEFENSIVE_PACT_CHAR = 19 # type: FontSymbols
	EATEN_FOOD_CHAR = 15 # type: FontSymbols
	GOLDEN_AGE_CHAR = 16 # type: FontSymbols
	GREAT_PEOPLE_CHAR = 12 # type: FontSymbols
	HAPPY_CHAR = 0 # type: FontSymbols
	HEALTHY_CHAR = 2 # type: FontSymbols
	MAP_CHAR = 20 # type: FontSymbols
	MAX_NUM_SYMBOLS = 23 # type: FontSymbols
	MOVES_CHAR = 6 # type: FontSymbols
	OCCUPATION_CHAR = 21 # type: FontSymbols
	OPEN_BORDERS_CHAR = 18 # type: FontSymbols
	POWER_CHAR = 22 # type: FontSymbols
	RELIGION_CHAR = 7 # type: FontSymbols
	SILVER_STAR_CHAR = 9 # type: FontSymbols
	STAR_CHAR = 8 # type: FontSymbols
	STRENGTH_CHAR = 5 # type: FontSymbols
	TRADE_CHAR = 10 # type: FontSymbols
	UNHAPPY_CHAR = 1 # type: FontSymbols
	UNHEALTHY_CHAR = 3 # type: FontSymbols

class FontTypes :
	GAME_FONT = 1 # type: FontTypes
	MENU_FONT = 3 # type: FontTypes
	MENU_HIGHLIGHT_FONT = 4 # type: FontTypes
	SMALL_FONT = 2 # type: FontTypes
	TITLE_FONT = 0 # type: FontTypes

class FootstepAudioTags :
	NO_FOOTSTEPAUDIO_TAG = -1 # type: FootstepAudioTags

class FootstepAudioTypes :
	NO_FOOTSTEPAUDIO = -1 # type: FootstepAudioTypes

class ForceControlTypes :
	FORCECONTROL_ADVANCED_START = 6 # type: ForceControlTypes
	FORCECONTROL_HANDICAP = 1 # type: ForceControlTypes
	FORCECONTROL_MAX_CITY_ELIMINATIONS = 5 # type: ForceControlTypes
	FORCECONTROL_MAX_TURNS = 4 # type: ForceControlTypes
	FORCECONTROL_OPTIONS = 2 # type: ForceControlTypes
	FORCECONTROL_SPEED = 0 # type: ForceControlTypes
	FORCECONTROL_VICTORIES = 3 # type: ForceControlTypes
	NO_FORCECONTROL = -1 # type: ForceControlTypes
	NUM_FORCECONTROL_TYPES = 7 # type: ForceControlTypes

def FreezeCamera( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def FullScreenCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class GameMessageTypes :
	GAMEMESSAGE_ADVANCED_START_ACTION = 92 # type: GameMessageTypes
	GAMEMESSAGE_APPLY_EVENT = 71 # type: GameMessageTypes
	GAMEMESSAGE_AUTH_REQUEST = 30 # type: GameMessageTypes
	GAMEMESSAGE_AUTH_RESPONSE = 31 # type: GameMessageTypes
	GAMEMESSAGE_AUTO_MISSION = 39 # type: GameMessageTypes
	GAMEMESSAGE_AUTO_MOVES = 35 # type: GameMessageTypes
	GAMEMESSAGE_CHANGE_VASSAL = 68 # type: GameMessageTypes
	GAMEMESSAGE_CHANGE_WAR = 67 # type: GameMessageTypes
	GAMEMESSAGE_CHAT = 48 # type: GameMessageTypes
	GAMEMESSAGE_CHOOSE_ELECTION = 69 # type: GameMessageTypes
	GAMEMESSAGE_CIV_CHOICE = 10 # type: GameMessageTypes
	GAMEMESSAGE_CIV_CHOICE_ACK = 13 # type: GameMessageTypes
	GAMEMESSAGE_CIV_CHOICE_NACK = 14 # type: GameMessageTypes
	GAMEMESSAGE_CIV_CHOSEN = 15 # type: GameMessageTypes
	GAMEMESSAGE_CLAIM_INFO = 12 # type: GameMessageTypes
	GAMEMESSAGE_CLEAR_TABLE = 82 # type: GameMessageTypes
	GAMEMESSAGE_CLOSE_CONNECTION = 58 # type: GameMessageTypes
	GAMEMESSAGE_CONFIRM_CIV_CLAIM = 11 # type: GameMessageTypes
	GAMEMESSAGE_CONTACT_CIV = 72 # type: GameMessageTypes
	GAMEMESSAGE_CONVERT = 47 # type: GameMessageTypes
	GAMEMESSAGE_DIPLOMACY = 87 # type: GameMessageTypes
	GAMEMESSAGE_DIPLOMACY_PROCESSED = 84 # type: GameMessageTypes
	GAMEMESSAGE_DIPLO_CHAT = 73 # type: GameMessageTypes
	GAMEMESSAGE_DIPLO_EVENT = 75 # type: GameMessageTypes
	GAMEMESSAGE_DIPLO_VOTE = 70 # type: GameMessageTypes
	GAMEMESSAGE_DO_COMMAND = 40 # type: GameMessageTypes
	GAMEMESSAGE_DO_TASK = 43 # type: GameMessageTypes
	GAMEMESSAGE_EMPIRE_SPLIT = 90 # type: GameMessageTypes
	GAMEMESSAGE_ESPIONAGE_CHANGE = 46 # type: GameMessageTypes
	GAMEMESSAGE_EVENT_TRIGGERED = 89 # type: GameMessageTypes
	GAMEMESSAGE_EXIT_TRADE = 78 # type: GameMessageTypes
	GAMEMESSAGE_EXTENDED_GAME = 34 # type: GameMessageTypes
	GAMEMESSAGE_FILE_INFO = 8 # type: GameMessageTypes
	GAMEMESSAGE_FOUND_RELIGION = 93 # type: GameMessageTypes
	GAMEMESSAGE_GAME_INFO = 24 # type: GameMessageTypes
	GAMEMESSAGE_GAME_TYPE = 6 # type: GameMessageTypes
	GAMEMESSAGE_HOT_DROP_NOTICE = 86 # type: GameMessageTypes
	GAMEMESSAGE_HOT_JOIN_NOTICE = 85 # type: GameMessageTypes
	GAMEMESSAGE_ID_ASSIGNMENT = 7 # type: GameMessageTypes
	GAMEMESSAGE_IMPLEMENT_OFFER = 66 # type: GameMessageTypes
	GAMEMESSAGE_INIT_GAME = 28 # type: GameMessageTypes
	GAMEMESSAGE_INIT_INFO = 17 # type: GameMessageTypes
	GAMEMESSAGE_INIT_PLAYERS = 29 # type: GameMessageTypes
	GAMEMESSAGE_INTERIM_NOTICE = 16 # type: GameMessageTypes
	GAMEMESSAGE_JOIN_GROUP = 37 # type: GameMessageTypes
	GAMEMESSAGE_KILL_DEAL = 79 # type: GameMessageTypes
	GAMEMESSAGE_LAUNCHING_INFO = 27 # type: GameMessageTypes
	GAMEMESSAGE_LAUNCH_SPACESHIP = 91 # type: GameMessageTypes
	GAMEMESSAGE_LINE_ENTITY = 51 # type: GameMessageTypes
	GAMEMESSAGE_LINE_ENTITY_DELETE = 53 # type: GameMessageTypes
	GAMEMESSAGE_LINE_GROUP_DELETE = 54 # type: GameMessageTypes
	GAMEMESSAGE_LOAD_GAME = 20 # type: GameMessageTypes
	GAMEMESSAGE_MAPSCRIPT_ACK = 19 # type: GameMessageTypes
	GAMEMESSAGE_MAPSCRIPT_CHECK = 18 # type: GameMessageTypes
	GAMEMESSAGE_MOD_NET_MESSAGE = 94 # type: GameMessageTypes
	GAMEMESSAGE_MP_DROP_INIT = 60 # type: GameMessageTypes
	GAMEMESSAGE_MP_DROP_RESULT = 63 # type: GameMessageTypes
	GAMEMESSAGE_MP_DROP_SAVE = 64 # type: GameMessageTypes
	GAMEMESSAGE_MP_DROP_UPDATE = 62 # type: GameMessageTypes
	GAMEMESSAGE_MP_DROP_VOTE = 61 # type: GameMessageTypes
	GAMEMESSAGE_MP_KICK = 56 # type: GameMessageTypes
	GAMEMESSAGE_MP_RETIRE = 57 # type: GameMessageTypes
	GAMEMESSAGE_NETWORK_READY = 0 # type: GameMessageTypes
	GAMEMESSAGE_NEVER_JOINED = 59 # type: GameMessageTypes
	GAMEMESSAGE_PAUSE = 55 # type: GameMessageTypes
	GAMEMESSAGE_PERCENT_CHANGE = 45 # type: GameMessageTypes
	GAMEMESSAGE_PICK_YOUR_CIV = 9 # type: GameMessageTypes
	GAMEMESSAGE_PING = 49 # type: GameMessageTypes
	GAMEMESSAGE_PITBOSS_INFO = 26 # type: GameMessageTypes
	GAMEMESSAGE_PLAYER_ID = 21 # type: GameMessageTypes
	GAMEMESSAGE_PLAYER_INFO = 23 # type: GameMessageTypes
	GAMEMESSAGE_PLAYER_OPTION = 33 # type: GameMessageTypes
	GAMEMESSAGE_POPUP = 88 # type: GameMessageTypes
	GAMEMESSAGE_POPUP_PROCESSED = 83 # type: GameMessageTypes
	GAMEMESSAGE_POP_ORDER = 42 # type: GameMessageTypes
	GAMEMESSAGE_PUSH_MISSION = 38 # type: GameMessageTypes
	GAMEMESSAGE_PUSH_ORDER = 41 # type: GameMessageTypes
	GAMEMESSAGE_REASSIGN_PLAYER = 25 # type: GameMessageTypes
	GAMEMESSAGE_RENEGOTIATE = 76 # type: GameMessageTypes
	GAMEMESSAGE_RENEGOTIATE_ITEM = 77 # type: GameMessageTypes
	GAMEMESSAGE_RESEARCH = 44 # type: GameMessageTypes
	GAMEMESSAGE_SAVE_FLAG_ACK = 2 # type: GameMessageTypes
	GAMEMESSAGE_SAVE_GAME = 80 # type: GameMessageTypes
	GAMEMESSAGE_SAVE_GAME_FLAG = 1 # type: GameMessageTypes
	GAMEMESSAGE_SEND_OFFER = 74 # type: GameMessageTypes
	GAMEMESSAGE_SIGN = 50 # type: GameMessageTypes
	GAMEMESSAGE_SIGN_DELETE = 52 # type: GameMessageTypes
	GAMEMESSAGE_SLOT_REASSIGNMENT = 22 # type: GameMessageTypes
	GAMEMESSAGE_SYNCH_START = 32 # type: GameMessageTypes
	GAMEMESSAGE_TOGGLE_TRADE = 65 # type: GameMessageTypes
	GAMEMESSAGE_TURN_COMPLETE = 36 # type: GameMessageTypes
	GAMEMESSAGE_UPDATE_CIVICS = 81 # type: GameMessageTypes
	GAMEMESSAGE_VERIFY_VERSION = 3 # type: GameMessageTypes
	GAMEMESSAGE_VERSION_NACK = 4 # type: GameMessageTypes
	GAMEMESSAGE_VERSION_WARNING = 5 # type: GameMessageTypes

class GameMode :
	GAMEMODE_NORMAL = 0 # type: GameMode
	GAMEMODE_PITBOSS = 1 # type: GameMode
	NO_GAMEMODE = -1 # type: GameMode
	NUM_GAMEMODES = 2 # type: GameMode

class GameOptionTypes :
	GAMEOPTION_ADVANCED_START = 0 # type: GameOptionTypes
	GAMEOPTION_AGGRESSIVE_AI = 6 # type: GameOptionTypes
	GAMEOPTION_ALWAYS_PEACE = 14 # type: GameOptionTypes
	GAMEOPTION_ALWAYS_WAR = 13 # type: GameOptionTypes
	GAMEOPTION_COMPLETE_KILLS = 19 # type: GameOptionTypes
	GAMEOPTION_FLIPPING_AFTER_CONQUEST = 3 # type: GameOptionTypes
	GAMEOPTION_LEAD_ANY_CIV = 7 # type: GameOptionTypes
	GAMEOPTION_LOCK_MODS = 18 # type: GameOptionTypes
	GAMEOPTION_NEW_RANDOM_SEED = 17 # type: GameOptionTypes
	GAMEOPTION_NO_BARBARIANS = 4 # type: GameOptionTypes
	GAMEOPTION_NO_CHANGING_WAR_PEACE = 16 # type: GameOptionTypes
	GAMEOPTION_NO_CITY_FLIPPING = 2 # type: GameOptionTypes
	GAMEOPTION_NO_CITY_RAZING = 1 # type: GameOptionTypes
	GAMEOPTION_NO_ESPIONAGE = 23 # type: GameOptionTypes
	GAMEOPTION_NO_EVENTS = 22 # type: GameOptionTypes
	GAMEOPTION_NO_GOODY_HUTS = 21 # type: GameOptionTypes
	GAMEOPTION_NO_TECH_BROKERING = 11 # type: GameOptionTypes
	GAMEOPTION_NO_TECH_TRADING = 10 # type: GameOptionTypes
	GAMEOPTION_NO_VASSAL_STATES = 20 # type: GameOptionTypes
	GAMEOPTION_ONE_CITY_CHALLENGE = 15 # type: GameOptionTypes
	GAMEOPTION_PERMANENT_ALLIANCES = 12 # type: GameOptionTypes
	GAMEOPTION_PICK_RELIGION = 9 # type: GameOptionTypes
	GAMEOPTION_RAGING_BARBARIANS = 5 # type: GameOptionTypes
	GAMEOPTION_RANDOM_PERSONALITIES = 8 # type: GameOptionTypes
	NO_GAMEOPTION = -1 # type: GameOptionTypes
	NUM_GAMEOPTION_TYPES = 24 # type: GameOptionTypes

class GameSpeedTypes :
	NO_GAMESPEED = -1 # type: GameSpeedTypes

class GameStateTypes :
	GAMESTATE_EXTENDED = 2 # type: GameStateTypes
	GAMESTATE_ON = 0 # type: GameStateTypes
	GAMESTATE_OVER = 1 # type: GameStateTypes

def GameToggleDiplomacyLoggingCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class GameTurnInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def iMonthIncrement( self ) :
		# type: () -> Any
		pass
	@iMonthIncrement.setter
	def iMonthIncrement( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iNumGameTurnsPerIncrement( self ) :
		# type: () -> Any
		pass
	@iNumGameTurnsPerIncrement.setter
	def iNumGameTurnsPerIncrement( self, value ) :
		# type: (Any) -> None
		pass

class GameType :
	GAME_HOTSEAT_LOAD = 8 # type: GameType
	GAME_HOTSEAT_NEW = 6 # type: GameType
	GAME_HOTSEAT_SCENARIO = 7 # type: GameType
	GAME_MP_LOAD = 5 # type: GameType
	GAME_MP_NEW = 3 # type: GameType
	GAME_MP_SCENARIO = 4 # type: GameType
	GAME_NONE = -1 # type: GameType
	GAME_PBEM_LOAD = 11 # type: GameType
	GAME_PBEM_NEW = 9 # type: GameType
	GAME_PBEM_SCENARIO = 10 # type: GameType
	GAME_REPLAY = 12 # type: GameType
	GAME_SP_LOAD = 2 # type: GameType
	GAME_SP_NEW = 0 # type: GameType
	GAME_SP_SCENARIO = 1 # type: GameType
	NUM_GAMETYPES = 13 # type: GameType

def GamebryoCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class GenericButtonSizes :
	BUTTON_SIZE_16 = 3 # type: GenericButtonSizes
	BUTTON_SIZE_24 = 2 # type: GenericButtonSizes
	BUTTON_SIZE_32 = 1 # type: GenericButtonSizes
	BUTTON_SIZE_46 = 0 # type: GenericButtonSizes
	BUTTON_SIZE_CUSTOM = 4 # type: GenericButtonSizes

class GoodyTypes :
	NO_GOODY = -1 # type: GoodyTypes

class GraphicLevelTypes :
	GRAPHICLEVEL_CURRENT = 3 # type: GraphicLevelTypes
	GRAPHICLEVEL_HIGH = 0 # type: GraphicLevelTypes
	GRAPHICLEVEL_LOW = 2 # type: GraphicLevelTypes
	GRAPHICLEVEL_MEDIUM = 1 # type: GraphicLevelTypes
	NUM_GRAPHICLEVELS = 4 # type: GraphicLevelTypes

class GraphicOptionTypes :
	GRAPHICOPTION_CITY_DETAIL = 2 # type: GraphicOptionTypes
	GRAPHICOPTION_CITY_RADIUS = 12 # type: GraphicOptionTypes
	GRAPHICOPTION_EFFECTS_DISABLED = 6 # type: GraphicOptionTypes
	GRAPHICOPTION_FROZEN_ANIMATIONS = 5 # type: GraphicOptionTypes
	GRAPHICOPTION_FULLSCREEN = 8 # type: GraphicOptionTypes
	GRAPHICOPTION_GLOBE_VIEW_BUILDINGS_DISABLED = 7 # type: GraphicOptionTypes
	GRAPHICOPTION_HEALTH_BARS = 1 # type: GraphicOptionTypes
	GRAPHICOPTION_HIRES_TERRAIN = 10 # type: GraphicOptionTypes
	GRAPHICOPTION_LOWRES_TEXTURES = 9 # type: GraphicOptionTypes
	GRAPHICOPTION_NO_COMBAT_ZOOM = 3 # type: GraphicOptionTypes
	GRAPHICOPTION_NO_ENEMY_GLOW = 4 # type: GraphicOptionTypes
	GRAPHICOPTION_NO_MOVIES = 11 # type: GraphicOptionTypes
	GRAPHICOPTION_SINGLE_UNIT_GRAPHICS = 0 # type: GraphicOptionTypes
	NO_GRAPHICOPTION = -1 # type: GraphicOptionTypes
	NUM_GRAPHICOPTION_TYPES = 13 # type: GraphicOptionTypes

class HandicapTypes :
	NO_HANDICAP = -1 # type: HandicapTypes

class HealthBarTypes :
	HEALTHBAR_ALIVE_ATTACK = 0 # type: HealthBarTypes
	HEALTHBAR_ALIVE_DEFEND = 1 # type: HealthBarTypes
	HEALTHBAR_DEAD = 2 # type: HealthBarTypes
	NUM_HEALTHBAR_TYPES = 3 # type: HealthBarTypes

def HideAllCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideBarsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideBeamsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideBonusesCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideBuildingsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideCityBillboardsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideCultureCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideCursorCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideDecalsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideEffectsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideEntitiesCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideFeaturesCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideFlagsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideGenericBuildingsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideHalfTilesCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideInterfaceCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideRoutesCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideSubUnitsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideSymbolsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideTerrainCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideUnitEntitiesCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideWaterCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def HideWavesCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class HitTestTypes :
	HITTEST_CHILDREN = 3 # type: HitTestTypes
	HITTEST_DEFAULT = 0 # type: HitTestTypes
	HITTEST_NOHIT = 4 # type: HitTestTypes
	HITTEST_ON = 1 # type: HitTestTypes
	HITTEST_SOLID = 2 # type: HitTestTypes

class HurryTypes :
	NO_HURRY = -1 # type: HurryTypes

class IDInfo( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def eOwner( self ) :
		# type: () -> Any
		pass
	@eOwner.setter
	def eOwner( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iID( self ) :
		# type: () -> Any
		pass
	@iID.setter
	def iID( self, value ) :
		# type: (Any) -> None
		pass

class ImprovementTypes :
	NO_IMPROVEMENT = -1 # type: ImprovementTypes

class InfoBarTypes :
	INFOBAR_EMPTY = 3 # type: InfoBarTypes
	INFOBAR_RATE = 1 # type: InfoBarTypes
	INFOBAR_RATE_EXTRA = 2 # type: InfoBarTypes
	INFOBAR_STORED = 0 # type: InfoBarTypes
	NUM_INFOBAR_TYPES = 4 # type: InfoBarTypes

class InputTypes :
	KB_0 = 2 # type: InputTypes
	KB_1 = 3 # type: InputTypes
	KB_2 = 4 # type: InputTypes
	KB_3 = 5 # type: InputTypes
	KB_4 = 6 # type: InputTypes
	KB_5 = 7 # type: InputTypes
	KB_6 = 8 # type: InputTypes
	KB_7 = 9 # type: InputTypes
	KB_8 = 10 # type: InputTypes
	KB_9 = 11 # type: InputTypes
	KB_A = 13 # type: InputTypes
	KB_APOSTROPHE = 47 # type: InputTypes
	KB_AT = 87 # type: InputTypes
	KB_B = 14 # type: InputTypes
	KB_BACKSLASH = 50 # type: InputTypes
	KB_BACKSPACE = 40 # type: InputTypes
	KB_C = 15 # type: InputTypes
	KB_CAPSLOCK = 58 # type: InputTypes
	KB_COLON = 89 # type: InputTypes
	KB_COMMA = 51 # type: InputTypes
	KB_D = 16 # type: InputTypes
	KB_DELETE = 108 # type: InputTypes
	KB_DOWN = 105 # type: InputTypes
	KB_E = 17 # type: InputTypes
	KB_END = 104 # type: InputTypes
	KB_EQUALS = 39 # type: InputTypes
	KB_ESCAPE = 1 # type: InputTypes
	KB_F = 18 # type: InputTypes
	KB_F1 = 59 # type: InputTypes
	KB_F10 = 68 # type: InputTypes
	KB_F11 = 69 # type: InputTypes
	KB_F12 = 70 # type: InputTypes
	KB_F2 = 60 # type: InputTypes
	KB_F3 = 61 # type: InputTypes
	KB_F4 = 62 # type: InputTypes
	KB_F5 = 63 # type: InputTypes
	KB_F6 = 64 # type: InputTypes
	KB_F7 = 65 # type: InputTypes
	KB_F8 = 66 # type: InputTypes
	KB_F9 = 67 # type: InputTypes
	KB_G = 19 # type: InputTypes
	KB_GRAVE = 48 # type: InputTypes
	KB_H = 20 # type: InputTypes
	KB_HOME = 99 # type: InputTypes
	KB_I = 21 # type: InputTypes
	KB_INSERT = 107 # type: InputTypes
	KB_J = 22 # type: InputTypes
	KB_K = 23 # type: InputTypes
	KB_L = 24 # type: InputTypes
	KB_LALT = 56 # type: InputTypes
	KB_LBRACKET = 42 # type: InputTypes
	KB_LCONTROL = 45 # type: InputTypes
	KB_LEFT = 102 # type: InputTypes
	KB_LSHIFT = 49 # type: InputTypes
	KB_M = 25 # type: InputTypes
	KB_MINUS = 12 # type: InputTypes
	KB_N = 26 # type: InputTypes
	KB_NUMLOCK = 71 # type: InputTypes
	KB_NUMPAD0 = 73 # type: InputTypes
	KB_NUMPAD1 = 74 # type: InputTypes
	KB_NUMPAD2 = 75 # type: InputTypes
	KB_NUMPAD3 = 76 # type: InputTypes
	KB_NUMPAD4 = 77 # type: InputTypes
	KB_NUMPAD5 = 78 # type: InputTypes
	KB_NUMPAD6 = 79 # type: InputTypes
	KB_NUMPAD7 = 80 # type: InputTypes
	KB_NUMPAD8 = 81 # type: InputTypes
	KB_NUMPAD9 = 82 # type: InputTypes
	KB_NUMPADCOMMA = 94 # type: InputTypes
	KB_NUMPADENTER = 90 # type: InputTypes
	KB_NUMPADEQUALS = 86 # type: InputTypes
	KB_NUMPADMINUS = 83 # type: InputTypes
	KB_NUMPADPERIOD = 85 # type: InputTypes
	KB_NUMPADPLUS = 84 # type: InputTypes
	KB_NUMPADSLASH = 95 # type: InputTypes
	KB_NUMPADSTAR = 55 # type: InputTypes
	KB_O = 27 # type: InputTypes
	KB_P = 28 # type: InputTypes
	KB_PAUSE = 98 # type: InputTypes
	KB_PERIOD = 52 # type: InputTypes
	KB_PGDN = 106 # type: InputTypes
	KB_PGUP = 101 # type: InputTypes
	KB_Q = 29 # type: InputTypes
	KB_R = 30 # type: InputTypes
	KB_RALT = 97 # type: InputTypes
	KB_RBRACKET = 43 # type: InputTypes
	KB_RCONTROL = 91 # type: InputTypes
	KB_RETURN = 44 # type: InputTypes
	KB_RIGHT = 103 # type: InputTypes
	KB_RSHIFT = 54 # type: InputTypes
	KB_S = 31 # type: InputTypes
	KB_SCROLL = 72 # type: InputTypes
	KB_SEMICOLON = 46 # type: InputTypes
	KB_SLASH = 53 # type: InputTypes
	KB_SPACE = 57 # type: InputTypes
	KB_SYSRQ = 96 # type: InputTypes
	KB_T = 32 # type: InputTypes
	KB_TAB = 41 # type: InputTypes
	KB_U = 33 # type: InputTypes
	KB_UNDERLINE = 88 # type: InputTypes
	KB_UP = 100 # type: InputTypes
	KB_V = 34 # type: InputTypes
	KB_VOLUMEDOWN = 92 # type: InputTypes
	KB_VOLUMEUP = 93 # type: InputTypes
	KB_W = 35 # type: InputTypes
	KB_X = 36 # type: InputTypes
	KB_Y = 37 # type: InputTypes
	KB_Z = 38 # type: InputTypes
	NUM_INPUT_TYPE = 116 # type: InputTypes

class InterfaceDirtyBits :
	Advanced_Start_DIRTY_BIT = 34 # type: InterfaceDirtyBits
	BlockadedPlots_DIRTY_BIT = 28 # type: InterfaceDirtyBits
	Center_DIRTY_BIT = 12 # type: InterfaceDirtyBits
	CitizenButtons_DIRTY_BIT = 9 # type: InterfaceDirtyBits
	CityInfo_DIRTY_BIT = 20 # type: InterfaceDirtyBits
	CityScreen_DIRTY_BIT = 23 # type: InterfaceDirtyBits
	ColoredPlots_DIRTY_BIT = 27 # type: InterfaceDirtyBits
	Cursor_DIRTY_BIT = 19 # type: InterfaceDirtyBits
	Domestic_Advisor_DIRTY_BIT = 32 # type: InterfaceDirtyBits
	Espionage_Advisor_DIRTY_BIT = 33 # type: InterfaceDirtyBits
	Event_DIRTY_BIT = 11 # type: InterfaceDirtyBits
	Financial_Screen_DIRTY_BIT = 29 # type: InterfaceDirtyBits
	Flag_DIRTY_BIT = 25 # type: InterfaceDirtyBits
	Fog_DIRTY_BIT = 1 # type: InterfaceDirtyBits
	Foreign_Screen_DIRTY_BIT = 30 # type: InterfaceDirtyBits
	GameData_DIRTY_BIT = 13 # type: InterfaceDirtyBits
	GlobeInfo_DIRTY_BIT = 3 # type: InterfaceDirtyBits
	GlobeLayer_DIRTY_BIT = 2 # type: InterfaceDirtyBits
	Help_DIRTY_BIT = 16 # type: InterfaceDirtyBits
	HighlightPlot_DIRTY_BIT = 26 # type: InterfaceDirtyBits
	InfoPane_DIRTY_BIT = 24 # type: InterfaceDirtyBits
	MinimapSection_DIRTY_BIT = 17 # type: InterfaceDirtyBits
	MiscButtons_DIRTY_BIT = 6 # type: InterfaceDirtyBits
	NUM_INTERFACE_DIRTY_BITS = 35 # type: InterfaceDirtyBits
	PercentButtons_DIRTY_BIT = 5 # type: InterfaceDirtyBits
	PlotListButtons_DIRTY_BIT = 7 # type: InterfaceDirtyBits
	Popup_DIRTY_BIT = 22 # type: InterfaceDirtyBits
	ResearchButtons_DIRTY_BIT = 10 # type: InterfaceDirtyBits
	Score_DIRTY_BIT = 14 # type: InterfaceDirtyBits
	SelectionButtons_DIRTY_BIT = 8 # type: InterfaceDirtyBits
	SelectionCamera_DIRTY_BIT = 0 # type: InterfaceDirtyBits
	SelectionSound_DIRTY_BIT = 18 # type: InterfaceDirtyBits
	Soundtrack_DIRTY_BIT = 31 # type: InterfaceDirtyBits
	TurnTimer_DIRTY_BIT = 15 # type: InterfaceDirtyBits
	UnitInfo_DIRTY_BIT = 21 # type: InterfaceDirtyBits
	Waypoints_DIRTY_BIT = 4 # type: InterfaceDirtyBits

class InterfaceMessageTypes :
	MESSAGE_TYPE_CHAT = 4 # type: InterfaceMessageTypes
	MESSAGE_TYPE_COMBAT_MESSAGE = 5 # type: InterfaceMessageTypes
	MESSAGE_TYPE_DISPLAY_ONLY = 1 # type: InterfaceMessageTypes
	MESSAGE_TYPE_INFO = 0 # type: InterfaceMessageTypes
	MESSAGE_TYPE_MAJOR_EVENT = 2 # type: InterfaceMessageTypes
	MESSAGE_TYPE_MINOR_EVENT = 3 # type: InterfaceMessageTypes
	MESSAGE_TYPE_QUEST = 6 # type: InterfaceMessageTypes
	NO_MESSAGE_TYPE = -1 # type: InterfaceMessageTypes
	NUM_INTERFACE_MESSAGE_TYPES = 7 # type: InterfaceMessageTypes

class InterfaceModeTypes :
	INTERFACEMODE_AIRBOMB = 13 # type: InterfaceModeTypes
	INTERFACEMODE_AIRLIFT = 9 # type: InterfaceModeTypes
	INTERFACEMODE_AIRSTRIKE = 15 # type: InterfaceModeTypes
	INTERFACEMODE_GLOBELAYER_INPUT = 4 # type: InterfaceModeTypes
	INTERFACEMODE_GO_TO = 5 # type: InterfaceModeTypes
	INTERFACEMODE_GO_TO_ALL = 7 # type: InterfaceModeTypes
	INTERFACEMODE_GO_TO_TYPE = 6 # type: InterfaceModeTypes
	INTERFACEMODE_GRIP = 3 # type: InterfaceModeTypes
	INTERFACEMODE_NUKE = 10 # type: InterfaceModeTypes
	INTERFACEMODE_PARADROP = 12 # type: InterfaceModeTypes
	INTERFACEMODE_PING = 1 # type: InterfaceModeTypes
	INTERFACEMODE_PYTHON_PICK_PLOT = 17 # type: InterfaceModeTypes
	INTERFACEMODE_RANGE_ATTACK = 14 # type: InterfaceModeTypes
	INTERFACEMODE_REBASE = 16 # type: InterfaceModeTypes
	INTERFACEMODE_RECON = 11 # type: InterfaceModeTypes
	INTERFACEMODE_ROUTE_TO = 8 # type: InterfaceModeTypes
	INTERFACEMODE_SAVE_PLOT_NIFS = 18 # type: InterfaceModeTypes
	INTERFACEMODE_SELECTION = 0 # type: InterfaceModeTypes
	INTERFACEMODE_SIGN = 2 # type: InterfaceModeTypes
	NO_INTERFACEMODE = -1 # type: InterfaceModeTypes
	NUM_INTERFACEMODE_TYPES = 19 # type: InterfaceModeTypes

class InterfaceVisibility :
	INTERFACE_ADVANCED_START = 4 # type: InterfaceVisibility
	INTERFACE_HIDE = 1 # type: InterfaceVisibility
	INTERFACE_HIDE_ALL = 2 # type: InterfaceVisibility
	INTERFACE_MINIMAP_ONLY = 3 # type: InterfaceVisibility
	INTERFACE_SHOW = 0 # type: InterfaceVisibility

class InvisibleTypes :
	NO_INVISIBLE = -1 # type: InvisibleTypes

class JustificationTypes :
	DLL_FONT_ADDITIVE = 16 # type: JustificationTypes
	DLL_FONT_CENTER_JUSTIFY = 4 # type: JustificationTypes
	DLL_FONT_CENTER_VERTICALLY = 8 # type: JustificationTypes
	DLL_FONT_LEFT_JUSTIFY = 1 # type: JustificationTypes
	DLL_FONT_RIGHT_JUSTIFY = 2 # type: JustificationTypes

class LeaderHeadTypes :
	NO_LEADER = -1 # type: LeaderHeadTypes

class LeaderheadAction :
	LEADERANIM_AGREE = 7 # type: LeaderheadAction
	LEADERANIM_ANNOYED = 4 # type: LeaderheadAction
	LEADERANIM_CAUTIOUS = 3 # type: LeaderheadAction
	LEADERANIM_DISAGREE = 6 # type: LeaderheadAction
	LEADERANIM_FRIENDLY = 1 # type: LeaderheadAction
	LEADERANIM_FURIOUS = 5 # type: LeaderheadAction
	LEADERANIM_GREETING = 0 # type: LeaderheadAction
	LEADERANIM_PLEASED = 2 # type: LeaderheadAction
	NO_LEADERANIM = -1 # type: LeaderheadAction
	NUM_LEADERANIM_TYPES = 8 # type: LeaderheadAction

class LoadType :
	LOAD_GAMETYPE = 3 # type: LoadType
	LOAD_INIT = 1 # type: LoadType
	LOAD_NORMAL = 0 # type: LoadType
	LOAD_REPLAY = 4 # type: LoadType
	LOAD_SETUP = 2 # type: LoadType

def LockQuadTreeVisCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class MemoryTypes :
	MEMORY_ACCEPTED_CIVIC = 14 # type: MemoryTypes
	MEMORY_ACCEPTED_JOIN_WAR = 16 # type: MemoryTypes
	MEMORY_ACCEPTED_RELIGION = 12 # type: MemoryTypes
	MEMORY_ACCEPTED_STOP_TRADING = 18 # type: MemoryTypes
	MEMORY_ACCEPT_DEMAND = 10 # type: MemoryTypes
	MEMORY_CANCELLED_OPEN_BORDERS = 25 # type: MemoryTypes
	MEMORY_DECLARED_WAR = 0 # type: MemoryTypes
	MEMORY_DECLARED_WAR_ON_FRIEND = 1 # type: MemoryTypes
	MEMORY_DENIED_CIVIC = 15 # type: MemoryTypes
	MEMORY_DENIED_JOIN_WAR = 17 # type: MemoryTypes
	MEMORY_DENIED_RELIGION = 13 # type: MemoryTypes
	MEMORY_DENIED_STOP_TRADING = 19 # type: MemoryTypes
	MEMORY_EVENT_BAD_TO_US = 31 # type: MemoryTypes
	MEMORY_EVENT_GOOD_TO_US = 30 # type: MemoryTypes
	MEMORY_GIVE_HELP = 8 # type: MemoryTypes
	MEMORY_HIRED_TRADE_EMBARGO = 22 # type: MemoryTypes
	MEMORY_HIRED_WAR_ALLY = 2 # type: MemoryTypes
	MEMORY_LIBERATED_CITIES = 32 # type: MemoryTypes
	MEMORY_MADE_DEMAND = 23 # type: MemoryTypes
	MEMORY_MADE_DEMAND_RECENT = 24 # type: MemoryTypes
	MEMORY_NUKED_FRIEND = 4 # type: MemoryTypes
	MEMORY_NUKED_US = 3 # type: MemoryTypes
	MEMORY_RAZED_CITY = 5 # type: MemoryTypes
	MEMORY_RAZED_HOLY_CITY = 6 # type: MemoryTypes
	MEMORY_RECEIVED_TECH_FROM_ANY = 27 # type: MemoryTypes
	MEMORY_REFUSED_HELP = 9 # type: MemoryTypes
	MEMORY_REJECTED_DEMAND = 11 # type: MemoryTypes
	MEMORY_SPY_CAUGHT = 7 # type: MemoryTypes
	MEMORY_STOPPED_TRADING = 20 # type: MemoryTypes
	MEMORY_STOPPED_TRADING_RECENT = 21 # type: MemoryTypes
	MEMORY_TRADED_TECH_TO_US = 26 # type: MemoryTypes
	MEMORY_VOTED_AGAINST_US = 28 # type: MemoryTypes
	MEMORY_VOTED_FOR_US = 29 # type: MemoryTypes
	NUM_MEMORY_TYPES = 33 # type: MemoryTypes

class MinimapModeTypes :
	MINIMAPMODE_MILITARY = 3 # type: MinimapModeTypes
	MINIMAPMODE_REPLAY = 2 # type: MinimapModeTypes
	MINIMAPMODE_TERRAIN = 1 # type: MinimapModeTypes
	MINIMAPMODE_TERRITORY = 0 # type: MinimapModeTypes
	NO_MINIMAPMODE = -1 # type: MinimapModeTypes
	NUM_MINIMAPMODE_TYPES = 4 # type: MinimapModeTypes

class MissionAITypes :
	MISSIONAI_ASSAULT = 20 # type: MissionAITypes
	MISSIONAI_ATTACK_SPY = 9 # type: MissionAITypes
	MISSIONAI_BLOCKADE = 16 # type: MissionAITypes
	MISSIONAI_BUILD = 19 # type: MissionAITypes
	MISSIONAI_CARRIER = 21 # type: MissionAITypes
	MISSIONAI_CONSTRUCT = 12 # type: MissionAITypes
	MISSIONAI_EXPLORE = 15 # type: MissionAITypes
	MISSIONAI_FOUND = 18 # type: MissionAITypes
	MISSIONAI_GREAT_WORK = 14 # type: MissionAITypes
	MISSIONAI_GROUP = 1 # type: MissionAITypes
	MISSIONAI_GUARD_BONUS = 6 # type: MissionAITypes
	MISSIONAI_GUARD_CITY = 5 # type: MissionAITypes
	MISSIONAI_GUARD_SPY = 8 # type: MissionAITypes
	MISSIONAI_GUARD_TRADE_NET = 7 # type: MissionAITypes
	MISSIONAI_HURRY = 13 # type: MissionAITypes
	MISSIONAI_LOAD_ASSAULT = 2 # type: MissionAITypes
	MISSIONAI_LOAD_SETTLER = 3 # type: MissionAITypes
	MISSIONAI_LOAD_SPECIAL = 4 # type: MissionAITypes
	MISSIONAI_PICKUP = 22 # type: MissionAITypes
	MISSIONAI_PILLAGE = 17 # type: MissionAITypes
	MISSIONAI_SHADOW = 0 # type: MissionAITypes
	MISSIONAI_SPREAD = 10 # type: MissionAITypes
	MISSIONAI_SPREAD_CORPORATION = 11 # type: MissionAITypes
	NO_MISSIONAI = -1 # type: MissionAITypes

class MissionData( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def eMissionType( self ) :
		# type: () -> Any
		pass
	@eMissionType.setter
	def eMissionType( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iData1( self ) :
		# type: () -> Any
		pass
	@iData1.setter
	def iData1( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iData2( self ) :
		# type: () -> Any
		pass
	@iData2.setter
	def iData2( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iFlags( self ) :
		# type: () -> Any
		pass
	@iFlags.setter
	def iFlags( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iPushTurn( self ) :
		# type: () -> Any
		pass
	@iPushTurn.setter
	def iPushTurn( self, value ) :
		# type: (Any) -> None
		pass

class MissionTypes :
	MISSION_AIRBOMB = 15 # type: MissionTypes
	MISSION_AIRLIFT = 11 # type: MissionTypes
	MISSION_AIRPATROL = 7 # type: MissionTypes
	MISSION_AIRSTRIKE = 39 # type: MissionTypes
	MISSION_BEGIN_COMBAT = 37 # type: MissionTypes
	MISSION_BOMBARD = 17 # type: MissionTypes
	MISSION_BUILD = 33 # type: MissionTypes
	MISSION_CAPTURED = 41 # type: MissionTypes
	MISSION_CONSTRUCT = 26 # type: MissionTypes
	MISSION_DAMAGE = 44 # type: MissionTypes
	MISSION_DESTROY = 20 # type: MissionTypes
	MISSION_DIE = 43 # type: MissionTypes
	MISSION_DISCOVER = 27 # type: MissionTypes
	MISSION_END_COMBAT = 38 # type: MissionTypes
	MISSION_ESPIONAGE = 35 # type: MissionTypes
	MISSION_FORTIFY = 5 # type: MissionTypes
	MISSION_FOUND = 22 # type: MissionTypes
	MISSION_GOLDEN_AGE = 32 # type: MissionTypes
	MISSION_GREAT_WORK = 30 # type: MissionTypes
	MISSION_HEAL = 9 # type: MissionTypes
	MISSION_HURRY = 28 # type: MissionTypes
	MISSION_IDLE = 42 # type: MissionTypes
	MISSION_INFILTRATE = 31 # type: MissionTypes
	MISSION_JOIN = 25 # type: MissionTypes
	MISSION_LEAD = 34 # type: MissionTypes
	MISSION_MOVE_TO = 0 # type: MissionTypes
	MISSION_MOVE_TO_UNIT = 2 # type: MissionTypes
	MISSION_MULTI_DESELECT = 46 # type: MissionTypes
	MISSION_MULTI_SELECT = 45 # type: MissionTypes
	MISSION_NUKE = 12 # type: MissionTypes
	MISSION_PARADROP = 14 # type: MissionTypes
	MISSION_PILLAGE = 18 # type: MissionTypes
	MISSION_PLUNDER = 6 # type: MissionTypes
	MISSION_RANGE_ATTACK = 16 # type: MissionTypes
	MISSION_RECON = 13 # type: MissionTypes
	MISSION_ROUTE_TO = 1 # type: MissionTypes
	MISSION_SABOTAGE = 19 # type: MissionTypes
	MISSION_SEAPATROL = 8 # type: MissionTypes
	MISSION_SENTRY = 10 # type: MissionTypes
	MISSION_SKIP = 3 # type: MissionTypes
	MISSION_SLEEP = 4 # type: MissionTypes
	MISSION_SPREAD = 23 # type: MissionTypes
	MISSION_SPREAD_CORPORATION = 24 # type: MissionTypes
	MISSION_STEAL_PLANS = 21 # type: MissionTypes
	MISSION_SURRENDER = 40 # type: MissionTypes
	MISSION_TRADE = 29 # type: MissionTypes
	NO_MISSION = -1 # type: MissionTypes
	NUM_MISSION_TYPES = 47 # type: MissionTypes

class MonthTypes :
	NO_MONTH = -1 # type: MonthTypes

class MouseFlags :
	MOUSE_CLICKED = 8986624 # type: MouseFlags
	MOUSE_CONTROL = 8 # type: MouseFlags
	MOUSE_DBLCLICKED = 35946496 # type: MouseFlags
	MOUSE_EVENT = 4096 # type: MouseFlags
	MOUSE_LBUTTON = 1 # type: MouseFlags
	MOUSE_LBUTTONDBLCLK = 32768 # type: MouseFlags
	MOUSE_LBUTTONDOWN = 8192 # type: MouseFlags
	MOUSE_LBUTTONUP = 16384 # type: MouseFlags
	MOUSE_MBUTTON = 16 # type: MouseFlags
	MOUSE_MBUTTONDBLCLK = 2097152 # type: MouseFlags
	MOUSE_MBUTTONDOWN = 524288 # type: MouseFlags
	MOUSE_MBUTTONUP = 1048576 # type: MouseFlags
	MOUSE_MOUSEMOVE = 4096 # type: MouseFlags
	MOUSE_MOUSEWHEELDOWN = 134217728 # type: MouseFlags
	MOUSE_MOUSEWHEELUP = 67108864 # type: MouseFlags
	MOUSE_RBUTTON = 2 # type: MouseFlags
	MOUSE_RBUTTONDBLCLK = 262144 # type: MouseFlags
	MOUSE_RBUTTONDOWN = 65536 # type: MouseFlags
	MOUSE_RBUTTONUP = 131072 # type: MouseFlags
	MOUSE_RELEASED = 17973248 # type: MouseFlags
	MOUSE_SHIFT = 4 # type: MouseFlags
	MOUSE_STATE = 1 # type: MouseFlags
	MOUSE_XBUTTON1 = 32 # type: MouseFlags
	MOUSE_XBUTTON2 = 64 # type: MouseFlags
	MOUSE_XBUTTONDBLCLK = 33554432 # type: MouseFlags
	MOUSE_XBUTTONDOWN = 8388608 # type: MouseFlags
	MOUSE_XBUTTONUP = 16777216 # type: MouseFlags

class MultiplayerOptionTypes :
	MPOPTION_ANONYMOUS = 3 # type: MultiplayerOptionTypes
	MPOPTION_SHUFFLE_TEAMS = 2 # type: MultiplayerOptionTypes
	MPOPTION_SIMULTANEOUS_TURNS = 0 # type: MultiplayerOptionTypes
	MPOPTION_TAKEOVER_AI = 1 # type: MultiplayerOptionTypes
	MPOPTION_TURN_TIMER = 4 # type: MultiplayerOptionTypes
	NO_MPOPTION = -1 # type: MultiplayerOptionTypes
	NUM_MPOPTION_TYPES = 5 # type: MultiplayerOptionTypes

def MusicCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class NetContactTypes :
	NETCONTACT_BUSY = 3 # type: NetContactTypes
	NETCONTACT_ESTABLISHED = 2 # type: NetContactTypes
	NETCONTACT_INITIAL = 0 # type: NetContactTypes
	NETCONTACT_RESPONSE = 1 # type: NetContactTypes
	NO_NETCONTACT = -1 # type: NetContactTypes
	NUM_NETCONTACT_TYPES = 4 # type: NetContactTypes

class NewConceptTypes :
	NO_NEW_CONCEPT = -1 # type: NewConceptTypes

class NiColorA( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def a( self ) :
		# type: () -> Any
		pass
	@a.setter
	def a( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def b( self ) :
		# type: () -> Any
		pass
	@b.setter
	def b( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def g( self ) :
		# type: () -> Any
		pass
	@g.setter
	def g( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def r( self ) :
		# type: () -> Any
		pass
	@r.setter
	def r( self, value ) :
		# type: (Any) -> None
		pass

class NiMatrix3( object ) :
	def GetEntry( self, arg0, arg1 ) :
		# type: (int, int) -> float
		pass
	def MakeIdentity( self ) :
		# type: () -> None
		pass
	def SetEntry( self, arg0, arg1, arg2 ) :
		# type: (int, int, float) -> None
		pass
	def __init__( self, *args, **kwargs ) :
		pass

class NiPoint2( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def x( self ) :
		# type: () -> Any
		pass
	@x.setter
	def x( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def y( self ) :
		# type: () -> Any
		pass
	@y.setter
	def y( self, value ) :
		# type: (Any) -> None
		pass

class NiPoint3( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def x( self ) :
		# type: () -> Any
		pass
	@x.setter
	def x( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def y( self ) :
		# type: () -> Any
		pass
	@y.setter
	def y( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def z( self ) :
		# type: () -> Any
		pass
	@z.setter
	def z( self, value ) :
		# type: (Any) -> None
		pass

def NiTextOut( *args, **kwargs ) :
	""" Places text onto the screen """

class NotifyCode :
	NOTIFY_CHARACTER = 6 # type: NotifyCode
	NOTIFY_CLICKED = 0 # type: NotifyCode
	NOTIFY_CURSOR_MOVE_OFF = 5 # type: NotifyCode
	NOTIFY_CURSOR_MOVE_ON = 4 # type: NotifyCode
	NOTIFY_DBL_CLICKED = 1 # type: NotifyCode
	NOTIFY_FLYOUT_ITEM_SELECTED = 12 # type: NotifyCode
	NOTIFY_FOCUS = 2 # type: NotifyCode
	NOTIFY_LINKEXECUTE = 18 # type: NotifyCode
	NOTIFY_LISTBOX_ITEM_SELECTED = 11 # type: NotifyCode
	NOTIFY_MOUSEMOVE = 12 # type: NotifyCode
	NOTIFY_MOUSEWHEELDOWN = 15 # type: NotifyCode
	NOTIFY_MOUSEWHEELUP = 14 # type: NotifyCode
	NOTIFY_MOVIE_DONE = 19 # type: NotifyCode
	NOTIFY_NEW_HORIZONTAL_STOP = 9 # type: NotifyCode
	NOTIFY_NEW_VERTICAL_STOP = 10 # type: NotifyCode
	NOTIFY_SCROLL_DOWN = 8 # type: NotifyCode
	NOTIFY_SCROLL_UP = 7 # type: NotifyCode
	NOTIFY_SLIDER_NEWSTOP = 20 # type: NotifyCode
	NOTIFY_TABLE_HEADER_SELECTED = 21 # type: NotifyCode
	NOTIFY_UNFOCUS = 3 # type: NotifyCode

class OrderData( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def bSave( self ) :
		# type: () -> Any
		pass
	@bSave.setter
	def bSave( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def eOrderType( self ) :
		# type: () -> Any
		pass
	@eOrderType.setter
	def eOrderType( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iData1( self ) :
		# type: () -> Any
		pass
	@iData1.setter
	def iData1( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iData2( self ) :
		# type: () -> Any
		pass
	@iData2.setter
	def iData2( self, value ) :
		# type: (Any) -> None
		pass

class OrderTypes :
	NO_ORDER = -1 # type: OrderTypes
	NUM_ORDER_TYPES = 4 # type: OrderTypes
	ORDER_CONSTRUCT = 1 # type: OrderTypes
	ORDER_CREATE = 2 # type: OrderTypes
	ORDER_MAINTAIN = 3 # type: OrderTypes
	ORDER_TRAIN = 0 # type: OrderTypes

class PBGameSetupData( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getCustomMapOption( self, *args, **kwargs ) :
		pass
	def getMPOptionAt( self, *args, **kwargs ) :
		pass
	def getMapName( self, *args, **kwargs ) :
		pass
	def getOptionAt( self, *args, **kwargs ) :
		pass
	def getVictory( self, *args, **kwargs ) :
		pass
	@property
	def iAdvancedStartPoints( self ) :
		# type: () -> Any
		pass
	@iAdvancedStartPoints.setter
	def iAdvancedStartPoints( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iCityElimination( self ) :
		# type: () -> Any
		pass
	@iCityElimination.setter
	def iCityElimination( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iClimate( self ) :
		# type: () -> Any
		pass
	@iClimate.setter
	def iClimate( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iEra( self ) :
		# type: () -> Any
		pass
	@iEra.setter
	def iEra( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iMaxTurns( self ) :
		# type: () -> Any
		pass
	@iMaxTurns.setter
	def iMaxTurns( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iNumCustomMapOptions( self ) :
		# type: () -> Any
		pass
	@iNumCustomMapOptions.setter
	def iNumCustomMapOptions( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iNumVictories( self ) :
		# type: () -> Any
		pass
	@iNumVictories.setter
	def iNumVictories( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iSeaLevel( self ) :
		# type: () -> Any
		pass
	@iSeaLevel.setter
	def iSeaLevel( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iSize( self ) :
		# type: () -> Any
		pass
	@iSize.setter
	def iSize( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iSpeed( self ) :
		# type: () -> Any
		pass
	@iSpeed.setter
	def iSpeed( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iTurnTime( self ) :
		# type: () -> Any
		pass
	@iTurnTime.setter
	def iTurnTime( self, value ) :
		# type: (Any) -> None
		pass

class PBPlayerAdminData( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def bClaimed( self ) :
		# type: () -> Any
		pass
	@bClaimed.setter
	def bClaimed( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def bHuman( self ) :
		# type: () -> Any
		pass
	@bHuman.setter
	def bHuman( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def bTurnActive( self ) :
		# type: () -> Any
		pass
	@bTurnActive.setter
	def bTurnActive( self, value ) :
		# type: (Any) -> None
		pass
	def getName( self, *args, **kwargs ) :
		pass
	def getPing( self, *args, **kwargs ) :
		pass
	def getScore( self, *args, **kwargs ) :
		pass

class PBPlayerSetupData( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	def getStatusText( self, *args, **kwargs ) :
		pass
	@property
	def iCiv( self ) :
		# type: () -> Any
		pass
	@iCiv.setter
	def iCiv( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iDifficulty( self ) :
		# type: () -> Any
		pass
	@iDifficulty.setter
	def iDifficulty( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iLeader( self ) :
		# type: () -> Any
		pass
	@iLeader.setter
	def iLeader( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iTeam( self ) :
		# type: () -> Any
		pass
	@iTeam.setter
	def iTeam( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iWho( self ) :
		# type: () -> Any
		pass
	@iWho.setter
	def iWho( self, value ) :
		# type: (Any) -> None
		pass

def PFEnableCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def PFUpdateCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class POINT( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def x( self ) :
		# type: () -> Any
		pass
	@x.setter
	def x( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def y( self ) :
		# type: () -> Any
		pass
	@y.setter
	def y( self, value ) :
		# type: (Any) -> None
		pass

class PanelStyles :
	PANEL_STYLE_BLUE50 = 12 # type: PanelStyles
	PANEL_STYLE_BLUELARGE = 11 # type: PanelStyles
	PANEL_STYLE_BOTTOMBAR = 14 # type: PanelStyles
	PANEL_STYLE_CITY_COLUMNC = 31 # type: PanelStyles
	PANEL_STYLE_CITY_COLUMNL = 30 # type: PanelStyles
	PANEL_STYLE_CITY_COLUMNR = 32 # type: PanelStyles
	PANEL_STYLE_CITY_INFO = 27 # type: PanelStyles
	PANEL_STYLE_CITY_LEFT = 23 # type: PanelStyles
	PANEL_STYLE_CITY_RIGHT = 24 # type: PanelStyles
	PANEL_STYLE_CITY_TANSHADE = 26 # type: PanelStyles
	PANEL_STYLE_CITY_TANTL = 28 # type: PanelStyles
	PANEL_STYLE_CITY_TANTR = 29 # type: PanelStyles
	PANEL_STYLE_CITY_TITLE = 33 # type: PanelStyles
	PANEL_STYLE_CITY_TOP = 25 # type: PanelStyles
	PANEL_STYLE_CIVILPEDIA = 8 # type: PanelStyles
	PANEL_STYLE_DAWN = 34 # type: PanelStyles
	PANEL_STYLE_DAWNBOTTOM = 36 # type: PanelStyles
	PANEL_STYLE_DAWNTOP = 35 # type: PanelStyles
	PANEL_STYLE_DEFAULT = 7 # type: PanelStyles
	PANEL_STYLE_EMPTY = 2 # type: PanelStyles
	PANEL_STYLE_EXTERNAL = 6 # type: PanelStyles
	PANEL_STYLE_FLAT = 3 # type: PanelStyles
	PANEL_STYLE_GAMEHUD_CENTER = 18 # type: PanelStyles
	PANEL_STYLE_GAMEHUD_LEFT = 16 # type: PanelStyles
	PANEL_STYLE_GAMEHUD_RIGHT = 17 # type: PanelStyles
	PANEL_STYLE_GAMEHUD_STATS = 19 # type: PanelStyles
	PANEL_STYLE_GAME_MAP = 20 # type: PanelStyles
	PANEL_STYLE_GAME_TOPBAR = 21 # type: PanelStyles
	PANEL_STYLE_HUD_HELP = 22 # type: PanelStyles
	PANEL_STYLE_IN = 4 # type: PanelStyles
	PANEL_STYLE_MAIN = 37 # type: PanelStyles
	PANEL_STYLE_MAIN_BLACK25 = 38 # type: PanelStyles
	PANEL_STYLE_MAIN_BLACK50 = 39 # type: PanelStyles
	PANEL_STYLE_MAIN_BOTTOMBAR = 48 # type: PanelStyles
	PANEL_STYLE_MAIN_SELECT = 49 # type: PanelStyles
	PANEL_STYLE_MAIN_TAN = 42 # type: PanelStyles
	PANEL_STYLE_MAIN_TAN15 = 43 # type: PanelStyles
	PANEL_STYLE_MAIN_TANB = 47 # type: PanelStyles
	PANEL_STYLE_MAIN_TANL = 44 # type: PanelStyles
	PANEL_STYLE_MAIN_TANR = 45 # type: PanelStyles
	PANEL_STYLE_MAIN_TANT = 46 # type: PanelStyles
	PANEL_STYLE_MAIN_WHITE = 40 # type: PanelStyles
	PANEL_STYLE_MAIN_WHITETAB = 41 # type: PanelStyles
	PANEL_STYLE_OUT = 5 # type: PanelStyles
	PANEL_STYLE_SOLID = 1 # type: PanelStyles
	PANEL_STYLE_STANDARD = 0 # type: PanelStyles
	PANEL_STYLE_STONE = 9 # type: PanelStyles
	PANEL_STYLE_TECH = 15 # type: PanelStyles
	PANEL_STYLE_TOPBAR = 13 # type: PanelStyles
	PANEL_STYLE_UNITSTAT = 10 # type: PanelStyles

def PauseEngineCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class PlayerColorTypes :
	NO_PLAYERCOLOR = -1 # type: PlayerColorTypes

class PlayerOptionTypes :
	NO_PLAYEROPTION = -1 # type: PlayerOptionTypes
	NUM_PLAYEROPTION_TYPES = 22 # type: PlayerOptionTypes
	PLAYEROPTION_ADVISOR_HELP = 1 # type: PlayerOptionTypes
	PLAYEROPTION_ADVISOR_POPUPS = 0 # type: PlayerOptionTypes
	PLAYEROPTION_AUTO_PROMOTION = 10 # type: PlayerOptionTypes
	PLAYEROPTION_LEAVE_FORESTS = 17 # type: PlayerOptionTypes
	PLAYEROPTION_MINIMIZE_POP_UPS = 3 # type: PlayerOptionTypes
	PLAYEROPTION_MISSIONARIES_AUTOMATED = 18 # type: PlayerOptionTypes
	PLAYEROPTION_MODDER_1 = 19 # type: PlayerOptionTypes
	PLAYEROPTION_MODDER_2 = 20 # type: PlayerOptionTypes
	PLAYEROPTION_MODDER_3 = 21 # type: PlayerOptionTypes
	PLAYEROPTION_NO_UNIT_CYCLING = 14 # type: PlayerOptionTypes
	PLAYEROPTION_NO_UNIT_RECOMMENDATIONS = 15 # type: PlayerOptionTypes
	PLAYEROPTION_NUMPAD_HELP = 13 # type: PlayerOptionTypes
	PLAYEROPTION_QUICK_ATTACK = 7 # type: PlayerOptionTypes
	PLAYEROPTION_QUICK_DEFENSE = 8 # type: PlayerOptionTypes
	PLAYEROPTION_QUICK_MOVES = 6 # type: PlayerOptionTypes
	PLAYEROPTION_RIGHT_CLICK_MENU = 16 # type: PlayerOptionTypes
	PLAYEROPTION_SAFE_AUTOMATION = 12 # type: PlayerOptionTypes
	PLAYEROPTION_SHOW_ENEMY_MOVES = 5 # type: PlayerOptionTypes
	PLAYEROPTION_SHOW_FRIENDLY_MOVES = 4 # type: PlayerOptionTypes
	PLAYEROPTION_STACK_ATTACK = 9 # type: PlayerOptionTypes
	PLAYEROPTION_START_AUTOMATED = 11 # type: PlayerOptionTypes
	PLAYEROPTION_WAIT_END_TURN = 2 # type: PlayerOptionTypes

class PlayerTypes :
	NO_PLAYER = -1 # type: PlayerTypes

class PlayerVoteTypes :
	NO_PLAYER_VOTE = -1 # type: PlayerVoteTypes
	NO_PLAYER_VOTE_CHECKED = -6 # type: PlayerVoteTypes
	PLAYER_VOTE_ABSTAIN = -4 # type: PlayerVoteTypes
	PLAYER_VOTE_NEVER = -5 # type: PlayerVoteTypes
	PLAYER_VOTE_NO = -3 # type: PlayerVoteTypes
	PLAYER_VOTE_YES = -2 # type: PlayerVoteTypes

class PlotLandscapeLayers :
	PLOT_LANDSCAPE_LAYER_ALL = -1 # type: PlotLandscapeLayers
	PLOT_LANDSCAPE_LAYER_BASE = 0 # type: PlotLandscapeLayers
	PLOT_LANDSCAPE_LAYER_NUMPAD_HELP = 2 # type: PlotLandscapeLayers
	PLOT_LANDSCAPE_LAYER_RECOMMENDED_PLOTS = 1 # type: PlotLandscapeLayers
	PLOT_LANDSCAPE_LAYER_REVEALED_PLOTS = 1 # type: PlotLandscapeLayers
	PLOT_LANDSCAPE_LAYER_WORLD_BUILDER = 2 # type: PlotLandscapeLayers

class PlotStyles :
	PLOT_STYLE_BOX_FILL = 16 # type: PlotStyles
	PLOT_STYLE_BOX_OUTLINE = 17 # type: PlotStyles
	PLOT_STYLE_CIRCLE = 21 # type: PlotStyles
	PLOT_STYLE_CIRCLES = 26 # type: PlotStyles
	PLOT_STYLE_DOTS = 25 # type: PlotStyles
	PLOT_STYLE_DOT_TARGET = 23 # type: PlotStyles
	PLOT_STYLE_NONE = -1 # type: PlotStyles
	PLOT_STYLE_NUMPAD_1 = 0 # type: PlotStyles
	PLOT_STYLE_NUMPAD_1_ANGLED = 8 # type: PlotStyles
	PLOT_STYLE_NUMPAD_2 = 1 # type: PlotStyles
	PLOT_STYLE_NUMPAD_2_ANGLED = 9 # type: PlotStyles
	PLOT_STYLE_NUMPAD_3 = 2 # type: PlotStyles
	PLOT_STYLE_NUMPAD_3_ANGLED = 10 # type: PlotStyles
	PLOT_STYLE_NUMPAD_4 = 3 # type: PlotStyles
	PLOT_STYLE_NUMPAD_4_ANGLED = 11 # type: PlotStyles
	PLOT_STYLE_NUMPAD_6 = 4 # type: PlotStyles
	PLOT_STYLE_NUMPAD_6_ANGLED = 12 # type: PlotStyles
	PLOT_STYLE_NUMPAD_7 = 5 # type: PlotStyles
	PLOT_STYLE_NUMPAD_7_ANGLED = 13 # type: PlotStyles
	PLOT_STYLE_NUMPAD_8 = 6 # type: PlotStyles
	PLOT_STYLE_NUMPAD_8_ANGLED = 14 # type: PlotStyles
	PLOT_STYLE_NUMPAD_9 = 7 # type: PlotStyles
	PLOT_STYLE_NUMPAD_9_ANGLED = 15 # type: PlotStyles
	PLOT_STYLE_RIVER_EAST = 19 # type: PlotStyles
	PLOT_STYLE_RIVER_SOUTH = 18 # type: PlotStyles
	PLOT_STYLE_SIDE_ARROWS = 20 # type: PlotStyles
	PLOT_STYLE_TARGET = 22 # type: PlotStyles
	PLOT_STYLE_WAVES = 24 # type: PlotStyles

class PlotTypes :
	NO_PLOT = -1 # type: PlotTypes
	NUM_PLOT_TYPES = 4 # type: PlotTypes
	PLOT_HILLS = 1 # type: PlotTypes
	PLOT_LAND = 2 # type: PlotTypes
	PLOT_OCEAN = 3 # type: PlotTypes
	PLOT_PEAK = 0 # type: PlotTypes

class PopupControlLayout :
	POPUP_LAYOUT_CENTER = 1 # type: PopupControlLayout
	POPUP_LAYOUT_LEFT = 0 # type: PopupControlLayout
	POPUP_LAYOUT_NUMLAYOUTS = 4 # type: PopupControlLayout
	POPUP_LAYOUT_RIGHT = 2 # type: PopupControlLayout
	POPUP_LAYOUT_STRETCH = 3 # type: PopupControlLayout

class PopupStates :
	POPUPSTATE_IMMEDIATE = 0 # type: PopupStates
	POPUPSTATE_MINIMIZED = 2 # type: PopupStates
	POPUPSTATE_QUEUED = 1 # type: PopupStates

class ProbabilityTypes :
	NO_PROBABILITY = -1 # type: ProbabilityTypes
	PROBABILITY_HIGH = 2 # type: ProbabilityTypes
	PROBABILITY_LOW = 0 # type: ProbabilityTypes
	PROBABILITY_REAL = 1 # type: ProbabilityTypes

class ProcessTypes :
	NO_PROCESS = -1 # type: ProcessTypes

def ProfilerCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def ProfilerResetMinMaxCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def ProfilerTurnLockOnCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class ProjectTypes :
	NO_PROJECT = -1 # type: ProjectTypes

class PromotionTypes :
	NO_PROMOTION = -1 # type: PromotionTypes

def RSEnableCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def RedrawGlobeViewCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def RedrawMinimapCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class ReligionTypes :
	NO_RELIGION = -1 # type: ReligionTypes

class ReplayMessageTypes :
	NO_REPLAY_MESSAGE = -1 # type: ReplayMessageTypes
	NUM_REPLAY_MESSAGE_TYPES = 3 # type: ReplayMessageTypes
	REPLAY_MESSAGE_CITY_FOUNDED = 1 # type: ReplayMessageTypes
	REPLAY_MESSAGE_MAJOR_EVENT = 0 # type: ReplayMessageTypes
	REPLAY_MESSAGE_PLOT_OWNER_CHANGE = 2 # type: ReplayMessageTypes

class RiverTypes :
	NO_RIVER = -1 # type: RiverTypes

class RouteTypes :
	NO_ROUTE = -1 # type: RouteTypes

class SaveGameTypes :
	NUM_SAVEGAME_TYPES = 9 # type: SaveGameTypes
	SAVEGAME_AUTO = 0 # type: SaveGameTypes
	SAVEGAME_DROP_CONTINUE = 6 # type: SaveGameTypes
	SAVEGAME_DROP_QUIT = 5 # type: SaveGameTypes
	SAVEGAME_GROUP = 4 # type: SaveGameTypes
	SAVEGAME_NONE = -1 # type: SaveGameTypes
	SAVEGAME_NORMAL = 3 # type: SaveGameTypes
	SAVEGAME_PBEM = 7 # type: SaveGameTypes
	SAVEGAME_QUICK = 2 # type: SaveGameTypes
	SAVEGAME_RECOVERY = 1 # type: SaveGameTypes
	SAVEGAME_REPLAY = 8 # type: SaveGameTypes

class SeaLevelTypes :
	NO_SEALEVEL = -1 # type: SeaLevelTypes

class SeasonTypes :
	NO_SEASON = -1 # type: SeasonTypes

def ShaderDescCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def ShowEntityBoundingSpheresCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def ShowOnlyAlphaSortingCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def ShowTerrainBoundingSpheresCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

def SlowMotionCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class SpecialBuildingTypes :
	NO_SPECIALBUILDING = -1 # type: SpecialBuildingTypes

class SpecialOptionTypes :
	NO_SPECIALOPTION = -1 # type: SpecialOptionTypes
	NUM_SPECIALOPTION_TYPES = 1 # type: SpecialOptionTypes
	SPECIALOPTION_REPORT_STATS = 0 # type: SpecialOptionTypes

class SpecialUnitTypes :
	NO_SPECIALUNIT = -1 # type: SpecialUnitTypes

class SpecialistTypes :
	NO_SPECIALIST = -1 # type: SpecialistTypes

class SymbolTypes :
	NO_SYMBOL = -1 # type: SymbolTypes

class TabGroupTypes :
	NO_TABGROUP = -1 # type: TabGroupTypes
	NUM_TABGROUPS = 5 # type: TabGroupTypes
	TABGROUP_AUDIO = 3 # type: TabGroupTypes
	TABGROUP_CLOCK = 4 # type: TabGroupTypes
	TABGROUP_GAME = 0 # type: TabGroupTypes
	TABGROUP_GRAPHICS = 2 # type: TabGroupTypes
	TABGROUP_INPUT = 1 # type: TabGroupTypes

class TableStyles :
	TABLE_STYLE_ALTDEFAULT = 5 # type: TableStyles
	TABLE_STYLE_ALTEMPTY = 2 # type: TableStyles
	TABLE_STYLE_CITY = 3 # type: TableStyles
	TABLE_STYLE_EMPTY = 1 # type: TableStyles
	TABLE_STYLE_EMPTYSELECTINACTIVE = 4 # type: TableStyles
	TABLE_STYLE_STAGINGROOM = 6 # type: TableStyles
	TABLE_STYLE_STANDARD = 0 # type: TableStyles

class TaskTypes :
	NUM_TASK_TYPES = 15 # type: TaskTypes
	TASK_CHANGE_SPECIALIST = 6 # type: TaskTypes
	TASK_CHANGE_WORKING_PLOT = 7 # type: TaskTypes
	TASK_CLEAR_ORDERS = 11 # type: TaskTypes
	TASK_CLEAR_RALLY_PLOT = 13 # type: TaskTypes
	TASK_CLEAR_WORKING_OVERRIDE = 8 # type: TaskTypes
	TASK_CONSCRIPT = 9 # type: TaskTypes
	TASK_DISBAND = 1 # type: TaskTypes
	TASK_GIFT = 2 # type: TaskTypes
	TASK_HURRY = 9 # type: TaskTypes
	TASK_LIBERATE = 14 # type: TaskTypes
	TASK_RALLY_PLOT = 12 # type: TaskTypes
	TASK_RAZE = 0 # type: TaskTypes
	TASK_SET_AUTOMATED_CITIZENS = 3 # type: TaskTypes
	TASK_SET_AUTOMATED_PRODUCTION = 4 # type: TaskTypes
	TASK_SET_EMPHASIZE = 5 # type: TaskTypes

class TeamTypes :
	NO_TEAM = -1 # type: TeamTypes

class TechTypes :
	NO_TECH = -1 # type: TechTypes

def TerrainNormalsCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class TerrainTypes :
	NO_TERRAIN = -1 # type: TerrainTypes

def TestDebugText( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class ToolTipAlignTypes :
	TOOLTIP_BOTTOM_CENTER = 10 # type: ToolTipAlignTypes
	TOOLTIP_BOTTOM_INLEFT = 11 # type: ToolTipAlignTypes
	TOOLTIP_BOTTOM_INRIGHT = 9 # type: ToolTipAlignTypes
	TOOLTIP_BOTTOM_LEFT = 12 # type: ToolTipAlignTypes
	TOOLTIP_BOTTOM_RIGHT = 8 # type: ToolTipAlignTypes
	TOOLTIP_CENTER_LEFT = 14 # type: ToolTipAlignTypes
	TOOLTIP_CENTER_RIGHT = 6 # type: ToolTipAlignTypes
	TOOLTIP_INBOTTOM_LEFT = 13 # type: ToolTipAlignTypes
	TOOLTIP_INBOTTOM_RIGHT = 7 # type: ToolTipAlignTypes
	TOOLTIP_INTOP_LEFT = 15 # type: ToolTipAlignTypes
	TOOLTIP_INTOP_RIGHT = 5 # type: ToolTipAlignTypes
	TOOLTIP_TOP_CENTER = 2 # type: ToolTipAlignTypes
	TOOLTIP_TOP_INLEFT = 1 # type: ToolTipAlignTypes
	TOOLTIP_TOP_INRIGHT = 3 # type: ToolTipAlignTypes
	TOOLTIP_TOP_LEFT = 0 # type: ToolTipAlignTypes
	TOOLTIP_TOP_RIGHT = 4 # type: ToolTipAlignTypes

class TradeData( object ) :
	@property
	def ItemType( self ) :
		# type: () -> Any
		pass
	@ItemType.setter
	def ItemType( self, value ) :
		# type: (Any) -> None
		pass
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def bHidden( self ) :
		# type: () -> Any
		pass
	@bHidden.setter
	def bHidden( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def bOffering( self ) :
		# type: () -> Any
		pass
	@bOffering.setter
	def bOffering( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iData( self ) :
		# type: () -> Any
		pass
	@iData.setter
	def iData( self, value ) :
		# type: (Any) -> None
		pass

class TradeableItems :
	NO_TRADEABLE_ITEMS = -1 # type: TradeableItems
	NUM_BASIC_ITEMS = 9 # type: TradeableItems
	NUM_TRADEABLE_HEADINGS = 17 # type: TradeableItems
	NUM_TRADEABLE_ITEMS = 17 # type: TradeableItems
	TRADE_CITIES = 11 # type: TradeableItems
	TRADE_CIVIC = 15 # type: TradeableItems
	TRADE_DEFENSIVE_PACT = 6 # type: TradeableItems
	TRADE_EMBARGO = 14 # type: TradeableItems
	TRADE_GOLD = 0 # type: TradeableItems
	TRADE_GOLD_PER_TURN = 1 # type: TradeableItems
	TRADE_MAPS = 2 # type: TradeableItems
	TRADE_OPEN_BORDERS = 5 # type: TradeableItems
	TRADE_PEACE = 12 # type: TradeableItems
	TRADE_PEACE_TREATY = 8 # type: TradeableItems
	TRADE_PERMANENT_ALLIANCE = 7 # type: TradeableItems
	TRADE_RELIGION = 16 # type: TradeableItems
	TRADE_RESOURCES = 10 # type: TradeableItems
	TRADE_SURRENDER = 4 # type: TradeableItems
	TRADE_TECHNOLOGIES = 9 # type: TradeableItems
	TRADE_VASSAL = 3 # type: TradeableItems
	TRADE_WAR = 13 # type: TradeableItems

class TraitTypes :
	NO_TRAIT = -1 # type: TraitTypes

class TurnTimerTypes :
	NO_TURNTIMER = -1 # type: TurnTimerTypes

class UnitAITypes :
	NO_UNITAI = -1 # type: UnitAITypes
	NUM_UNITAI_TYPES = 41 # type: UnitAITypes
	UNITAI_ANIMAL = 1 # type: UnitAITypes
	UNITAI_ARTIST = 16 # type: UnitAITypes
	UNITAI_ASSAULT_SEA = 28 # type: UnitAITypes
	UNITAI_ATTACK = 4 # type: UnitAITypes
	UNITAI_ATTACK_AIR = 35 # type: UnitAITypes
	UNITAI_ATTACK_CITY = 5 # type: UnitAITypes
	UNITAI_ATTACK_CITY_LEMMING = 40 # type: UnitAITypes
	UNITAI_ATTACK_SEA = 24 # type: UnitAITypes
	UNITAI_CARRIER_AIR = 37 # type: UnitAITypes
	UNITAI_CARRIER_SEA = 32 # type: UnitAITypes
	UNITAI_CITY_COUNTER = 11 # type: UnitAITypes
	UNITAI_CITY_DEFENSE = 10 # type: UnitAITypes
	UNITAI_CITY_SPECIAL = 12 # type: UnitAITypes
	UNITAI_COLLATERAL = 6 # type: UnitAITypes
	UNITAI_COUNTER = 9 # type: UnitAITypes
	UNITAI_DEFENSE_AIR = 36 # type: UnitAITypes
	UNITAI_ENGINEER = 20 # type: UnitAITypes
	UNITAI_ESCORT_SEA = 26 # type: UnitAITypes
	UNITAI_EXPLORE = 13 # type: UnitAITypes
	UNITAI_EXPLORE_SEA = 27 # type: UnitAITypes
	UNITAI_GENERAL = 18 # type: UnitAITypes
	UNITAI_ICBM = 22 # type: UnitAITypes
	UNITAI_MERCHANT = 19 # type: UnitAITypes
	UNITAI_MISSILE_AIR = 38 # type: UnitAITypes
	UNITAI_MISSILE_CARRIER_SEA = 33 # type: UnitAITypes
	UNITAI_MISSIONARY = 14 # type: UnitAITypes
	UNITAI_MISSIONARY_SEA = 30 # type: UnitAITypes
	UNITAI_PARADROP = 39 # type: UnitAITypes
	UNITAI_PILLAGE = 7 # type: UnitAITypes
	UNITAI_PIRATE_SEA = 34 # type: UnitAITypes
	UNITAI_PROPHET = 15 # type: UnitAITypes
	UNITAI_RESERVE = 8 # type: UnitAITypes
	UNITAI_RESERVE_SEA = 25 # type: UnitAITypes
	UNITAI_SCIENTIST = 17 # type: UnitAITypes
	UNITAI_SETTLE = 2 # type: UnitAITypes
	UNITAI_SETTLER_SEA = 29 # type: UnitAITypes
	UNITAI_SPY = 21 # type: UnitAITypes
	UNITAI_SPY_SEA = 31 # type: UnitAITypes
	UNITAI_UNKNOWN = 0 # type: UnitAITypes
	UNITAI_WORKER = 3 # type: UnitAITypes
	UNITAI_WORKER_SEA = 23 # type: UnitAITypes

class UnitClassTypes :
	NO_UNITCLASS = -1 # type: UnitClassTypes

class UnitCombatTypes :
	NO_UNITCOMBAT = -1 # type: UnitCombatTypes

def UnitDebugMenuCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class UnitTypes :
	NO_UNIT = -1 # type: UnitTypes

class UpkeepTypes :
	NO_UPKEEP = -1 # type: UpkeepTypes

class VictoryTypes :
	NO_VICTORY = -1 # type: VictoryTypes

class VoiceTargetTypes :
	NO_VOICETARGET = -1 # type: VoiceTargetTypes
	NUM_VOICETARGETS = 3 # type: VoiceTargetTypes
	VOICETARGET_ALL = 2 # type: VoiceTargetTypes
	VOICETARGET_DIPLO = 0 # type: VoiceTargetTypes
	VOICETARGET_TEAM = 1 # type: VoiceTargetTypes

class VoteSourceTypes :
	NO_VOTESOURCE = -1 # type: VoteSourceTypes

class VoteTypes :
	NO_VOTE = -1 # type: VoteTypes

class WarPlanTypes :
	NO_WARPLAN = -1 # type: WarPlanTypes
	WARPLAN_ATTACKED = 1 # type: WarPlanTypes
	WARPLAN_ATTACKED_RECENT = 0 # type: WarPlanTypes
	WARPLAN_DOGPILE = 6 # type: WarPlanTypes
	WARPLAN_LIMITED = 4 # type: WarPlanTypes
	WARPLAN_PREPARING_LIMITED = 2 # type: WarPlanTypes
	WARPLAN_PREPARING_TOTAL = 3 # type: WarPlanTypes
	WARPLAN_TOTAL = 5 # type: WarPlanTypes

class WidgetAnim :
	WA_DISABLED = 9 # type: WidgetAnim
	WA_FOCUS = 1 # type: WidgetAnim
	WA_IDLE = 0 # type: WidgetAnim
	WA_LMB_CLICKED = 3 # type: WidgetAnim
	WA_LMB_RELEASED = 4 # type: WidgetAnim
	WA_MOUSE_OFF = 8 # type: WidgetAnim
	WA_MOUSE_OVER = 7 # type: WidgetAnim
	WA_RMB_CLICKED = 5 # type: WidgetAnim
	WA_RMB_RELEASED = 6 # type: WidgetAnim
	WA_UNFOCUS = 2 # type: WidgetAnim

class WidgetTypes :
	NUM_WIDGET_TYPES = 163 # type: WidgetTypes
	WIDGET_ACTION = 15 # type: WidgetTypes
	WIDGET_ANGRY_CITIZEN = 19 # type: WidgetTypes
	WIDGET_AUTOMATE_CITIZENS = 31 # type: WidgetTypes
	WIDGET_AUTOMATE_PRODUCTION = 32 # type: WidgetTypes
	WIDGET_CHANGE_PERCENT = 23 # type: WidgetTypes
	WIDGET_CHANGE_SPECIALIST = 20 # type: WidgetTypes
	WIDGET_CHOOSE_EVENT = 126 # type: WidgetTypes
	WIDGET_CITIZEN = 17 # type: WidgetTypes
	WIDGET_CITY_NAME = 4 # type: WidgetTypes
	WIDGET_CITY_SCROLL = 2 # type: WidgetTypes
	WIDGET_CITY_TAB = 24 # type: WidgetTypes
	WIDGET_CLOSE_SCREEN = 157 # type: WidgetTypes
	WIDGET_COMMERCE_MOD_HELP = 156 # type: WidgetTypes
	WIDGET_CONSCRIPT = 14 # type: WidgetTypes
	WIDGET_CONSTRUCT = 9 # type: WidgetTypes
	WIDGET_CONTACT_CIV = 25 # type: WidgetTypes
	WIDGET_CONVERT = 30 # type: WidgetTypes
	WIDGET_CREATE = 10 # type: WidgetTypes
	WIDGET_CREATE_GROUP = 6 # type: WidgetTypes
	WIDGET_DEAL_KILL = 151 # type: WidgetTypes
	WIDGET_DELETE_GROUP = 7 # type: WidgetTypes
	WIDGET_DIPLOMACY_RESPONSE = 34 # type: WidgetTypes
	WIDGET_DISABLED_CITIZEN = 16 # type: WidgetTypes
	WIDGET_EMPHASIZE = 33 # type: WidgetTypes
	WIDGET_END_TURN = 28 # type: WidgetTypes
	WIDGET_FILE_EDITBOX = 37 # type: WidgetTypes
	WIDGET_FILE_LISTBOX = 36 # type: WidgetTypes
	WIDGET_FLAG = 57 # type: WidgetTypes
	WIDGET_FOREIGN_ADVISOR = 147 # type: WidgetTypes
	WIDGET_FREE_CITIZEN = 18 # type: WidgetTypes
	WIDGET_GENERAL = 35 # type: WidgetTypes
	WIDGET_GLOBELAYER = 160 # type: WidgetTypes
	WIDGET_GLOBELAYER_OPTION = 161 # type: WidgetTypes
	WIDGET_GLOBELAYER_TOGGLE = 162 # type: WidgetTypes
	WIDGET_HELP_ADJUST = 106 # type: WidgetTypes
	WIDGET_HELP_BONUS_REVEAL = 110 # type: WidgetTypes
	WIDGET_HELP_BUILDING = 74 # type: WidgetTypes
	WIDGET_HELP_BUILD_BRIDGE = 100 # type: WidgetTypes
	WIDGET_HELP_CIVIC_REVEAL = 111 # type: WidgetTypes
	WIDGET_HELP_CORPORATION_CITY = 63 # type: WidgetTypes
	WIDGET_HELP_CULTURE = 70 # type: WidgetTypes
	WIDGET_HELP_DEFENSE = 65 # type: WidgetTypes
	WIDGET_HELP_DEFENSIVE_PACT = 97 # type: WidgetTypes
	WIDGET_HELP_DOMAIN_EXTRA_MOVES = 105 # type: WidgetTypes
	WIDGET_HELP_ESPIONAGE_COST = 76 # type: WidgetTypes
	WIDGET_HELP_FEATURE_PRODUCTION = 84 # type: WidgetTypes
	WIDGET_HELP_FINANCE_AWAY_SUPPLY = 117 # type: WidgetTypes
	WIDGET_HELP_FINANCE_CITY_MAINT = 118 # type: WidgetTypes
	WIDGET_HELP_FINANCE_CIVIC_UPKEEP = 119 # type: WidgetTypes
	WIDGET_HELP_FINANCE_FOREIGN_INCOME = 120 # type: WidgetTypes
	WIDGET_HELP_FINANCE_GOLD_RESERVE = 124 # type: WidgetTypes
	WIDGET_HELP_FINANCE_GROSS_INCOME = 122 # type: WidgetTypes
	WIDGET_HELP_FINANCE_INFLATED_COSTS = 121 # type: WidgetTypes
	WIDGET_HELP_FINANCE_NET_GOLD = 123 # type: WidgetTypes
	WIDGET_HELP_FINANCE_NUM_UNITS = 115 # type: WidgetTypes
	WIDGET_HELP_FINANCE_UNIT_COST = 116 # type: WidgetTypes
	WIDGET_HELP_FOUND_CORPORATION = 114 # type: WidgetTypes
	WIDGET_HELP_FOUND_RELIGION = 113 # type: WidgetTypes
	WIDGET_HELP_FREE_TECH = 89 # type: WidgetTypes
	WIDGET_HELP_FREE_UNIT = 83 # type: WidgetTypes
	WIDGET_HELP_GOLD_TRADE = 95 # type: WidgetTypes
	WIDGET_HELP_GREAT_GENERAL = 72 # type: WidgetTypes
	WIDGET_HELP_GREAT_PEOPLE = 71 # type: WidgetTypes
	WIDGET_HELP_HAPPINESS = 67 # type: WidgetTypes
	WIDGET_HELP_HAPPINESS_RATE = 88 # type: WidgetTypes
	WIDGET_HELP_HEALTH = 66 # type: WidgetTypes
	WIDGET_HELP_HEALTH_RATE = 87 # type: WidgetTypes
	WIDGET_HELP_IGNORE_IRRIGATION = 102 # type: WidgetTypes
	WIDGET_HELP_IMPROVEMENT = 104 # type: WidgetTypes
	WIDGET_HELP_IRRIGATION = 101 # type: WidgetTypes
	WIDGET_HELP_LOS_BONUS = 90 # type: WidgetTypes
	WIDGET_HELP_MAINTENANCE = 60 # type: WidgetTypes
	WIDGET_HELP_MAP_CENTER = 91 # type: WidgetTypes
	WIDGET_HELP_MAP_REVEAL = 92 # type: WidgetTypes
	WIDGET_HELP_MAP_TRADE = 93 # type: WidgetTypes
	WIDGET_HELP_MOVE_BONUS = 82 # type: WidgetTypes
	WIDGET_HELP_NATIONALITY = 64 # type: WidgetTypes
	WIDGET_HELP_OBSOLETE = 79 # type: WidgetTypes
	WIDGET_HELP_OBSOLETE_BONUS = 80 # type: WidgetTypes
	WIDGET_HELP_OBSOLETE_SPECIAL = 81 # type: WidgetTypes
	WIDGET_HELP_OPEN_BORDERS = 96 # type: WidgetTypes
	WIDGET_HELP_PERMANENT_ALLIANCE = 98 # type: WidgetTypes
	WIDGET_HELP_POPULATION = 68 # type: WidgetTypes
	WIDGET_HELP_PROCESS_INFO = 112 # type: WidgetTypes
	WIDGET_HELP_PRODUCTION = 69 # type: WidgetTypes
	WIDGET_HELP_PROMOTION = 125 # type: WidgetTypes
	WIDGET_HELP_RELIGION = 61 # type: WidgetTypes
	WIDGET_HELP_RELIGION_CITY = 62 # type: WidgetTypes
	WIDGET_HELP_SELECTED = 73 # type: WidgetTypes
	WIDGET_HELP_SPECIAL_BUILDING = 108 # type: WidgetTypes
	WIDGET_HELP_TECH_ENTRY = 77 # type: WidgetTypes
	WIDGET_HELP_TECH_PREPREQ = 78 # type: WidgetTypes
	WIDGET_HELP_TECH_TRADE = 94 # type: WidgetTypes
	WIDGET_HELP_TERRAIN_TRADE = 107 # type: WidgetTypes
	WIDGET_HELP_TRADE_ROUTES = 86 # type: WidgetTypes
	WIDGET_HELP_TRADE_ROUTE_CITY = 75 # type: WidgetTypes
	WIDGET_HELP_VASSAL_STATE = 99 # type: WidgetTypes
	WIDGET_HELP_WATER_WORK = 103 # type: WidgetTypes
	WIDGET_HELP_WORKER_RATE = 85 # type: WidgetTypes
	WIDGET_HELP_YIELD_CHANGE = 109 # type: WidgetTypes
	WIDGET_HURRY = 12 # type: WidgetTypes
	WIDGET_LAUNCH_VICTORY = 29 # type: WidgetTypes
	WIDGET_LEADERHEAD = 154 # type: WidgetTypes
	WIDGET_LEADER_LINE = 155 # type: WidgetTypes
	WIDGET_LIBERATE_CITY = 3 # type: WidgetTypes
	WIDGET_MAINTAIN = 11 # type: WidgetTypes
	WIDGET_MENU_ICON = 13 # type: WidgetTypes
	WIDGET_MINIMAP_HIGHLIGHT = 152 # type: WidgetTypes
	WIDGET_PEDIA_BACK = 132 # type: WidgetTypes
	WIDGET_PEDIA_DESCRIPTION = 149 # type: WidgetTypes
	WIDGET_PEDIA_DESCRIPTION_NO_HELP = 150 # type: WidgetTypes
	WIDGET_PEDIA_FORWARD = 133 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_BONUS = 134 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_BUILDING = 129 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_CIV = 140 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_CIVIC = 139 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_CORPORATION = 159 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_DERIVED_TECH = 131 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_FEATURE = 145 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_IMPROVEMENT = 138 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_LEADER = 141 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_PROJECT = 143 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_PROMOTION = 136 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_RELIGION = 158 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_REQUIRED_TECH = 130 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_SPECIALIST = 142 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_TECH = 127 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_TERRAIN = 144 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_UNIT = 128 # type: WidgetTypes
	WIDGET_PEDIA_JUMP_TO_UNIT_COMBAT = 137 # type: WidgetTypes
	WIDGET_PEDIA_MAIN = 135 # type: WidgetTypes
	WIDGET_PLOT_LIST = 0 # type: WidgetTypes
	WIDGET_PLOT_LIST_SHIFT = 1 # type: WidgetTypes
	WIDGET_POPUP_QUEUE = 58 # type: WidgetTypes
	WIDGET_PRODUCTION_MOD_HELP = 153 # type: WidgetTypes
	WIDGET_PYTHON = 59 # type: WidgetTypes
	WIDGET_RESEARCH = 21 # type: WidgetTypes
	WIDGET_REVOLUTION = 148 # type: WidgetTypes
	WIDGET_SCORE_BREAKDOWN = 26 # type: WidgetTypes
	WIDGET_TECH_TREE = 22 # type: WidgetTypes
	WIDGET_TRADE_ITEM = 55 # type: WidgetTypes
	WIDGET_TRAIN = 8 # type: WidgetTypes
	WIDGET_TURN_EVENT = 146 # type: WidgetTypes
	WIDGET_UNIT_MODEL = 56 # type: WidgetTypes
	WIDGET_UNIT_NAME = 5 # type: WidgetTypes
	WIDGET_WB_ALL_PLOTS_BUTTON = 42 # type: WidgetTypes
	WIDGET_WB_CITY_EDIT_BUTTON = 47 # type: WidgetTypes
	WIDGET_WB_DIPLOMACY_MODE_BUTTON = 51 # type: WidgetTypes
	WIDGET_WB_ERASE_BUTTON = 44 # type: WidgetTypes
	WIDGET_WB_EXIT_BUTTON = 45 # type: WidgetTypes
	WIDGET_WB_LANDMARK_BUTTON = 43 # type: WidgetTypes
	WIDGET_WB_LOAD_BUTTON = 41 # type: WidgetTypes
	WIDGET_WB_NORMAL_MAP_TAB_MODE_BUTTON = 49 # type: WidgetTypes
	WIDGET_WB_NORMAL_PLAYER_TAB_MODE_BUTTON = 48 # type: WidgetTypes
	WIDGET_WB_REGENERATE_MAP = 54 # type: WidgetTypes
	WIDGET_WB_REVEAL_ALL_BUTTON = 52 # type: WidgetTypes
	WIDGET_WB_REVEAL_TAB_MODE_BUTTON = 50 # type: WidgetTypes
	WIDGET_WB_SAVE_BUTTON = 40 # type: WidgetTypes
	WIDGET_WB_UNIT_EDIT_BUTTON = 46 # type: WidgetTypes
	WIDGET_WB_UNREVEAL_ALL_BUTTON = 53 # type: WidgetTypes
	WIDGET_ZOOM_CITY = 27 # type: WidgetTypes

def WireframeCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class WorldBuilderPopupTypes :
	NUM_WBPOPUP = 208 # type: WorldBuilderPopupTypes
	WBPOPUP_CITY = 200 # type: WorldBuilderPopupTypes
	WBPOPUP_FEATURE = 205 # type: WorldBuilderPopupTypes
	WBPOPUP_GAME = 207 # type: WorldBuilderPopupTypes
	WBPOPUP_IMPROVEMENT = 206 # type: WorldBuilderPopupTypes
	WBPOPUP_NONE = -1 # type: WorldBuilderPopupTypes
	WBPOPUP_PLAYER = 202 # type: WorldBuilderPopupTypes
	WBPOPUP_PLOT = 203 # type: WorldBuilderPopupTypes
	WBPOPUP_START = 200 # type: WorldBuilderPopupTypes
	WBPOPUP_TERRAIN = 204 # type: WorldBuilderPopupTypes
	WBPOPUP_UNIT = 201 # type: WorldBuilderPopupTypes

class WorldSizeTypes :
	NO_WORLDSIZE = -1 # type: WorldSizeTypes
	NUM_WORLDSIZE_TYPES = 6 # type: WorldSizeTypes
	WORLDSIZE_DUEL = 0 # type: WorldSizeTypes
	WORLDSIZE_HUGE = 5 # type: WorldSizeTypes
	WORLDSIZE_LARGE = 4 # type: WorldSizeTypes
	WORLDSIZE_SMALL = 2 # type: WorldSizeTypes
	WORLDSIZE_STANDARD = 3 # type: WorldSizeTypes
	WORLDSIZE_TINY = 1 # type: WorldSizeTypes

def WriteFogWarTextureCB( arg0, arg1 ) :
	# type: (bool, None) -> None
	pass

class XYCoords( object ) :
	def __init__( self, *args, **kwargs ) :
		pass
	@property
	def iX( self ) :
		# type: () -> Any
		pass
	@iX.setter
	def iX( self, value ) :
		# type: (Any) -> None
		pass
	@property
	def iY( self ) :
		# type: () -> Any
		pass
	@iY.setter
	def iY( self, value ) :
		# type: (Any) -> None
		pass

class YieldTypes :
	NO_YIELD = -1 # type: YieldTypes
	NUM_YIELD_TYPES = 3 # type: YieldTypes
	YIELD_COMMERCE = 2 # type: YieldTypes
	YIELD_FOOD = 0 # type: YieldTypes
	YIELD_PRODUCTION = 1 # type: YieldTypes

class ZoomLevelTypes :
	ZOOM_DETAIL = 1 # type: ZoomLevelTypes
	ZOOM_GLOBEVIEW = 8 # type: ZoomLevelTypes
	ZOOM_NORMAL = 2 # type: ZoomLevelTypes
	ZOOM_UNKNOWN = 0 # type: ZoomLevelTypes

def addImportModule( *args, **kwargs ) :
	pass

def addWBAdvancedStartControlTabs(  ) :
	# type: () -> cyAddWBAdvancedStartControlTabs
	""" inits the worldbuilder tool AdvancedStart control """

def addWBPlayerControlTabs(  ) :
	# type: () -> cyAddWBPlayerControlTabs
	""" inits the worldbuilder tool player control """

def atWar( arg0, arg1 ) :
	# type: (int, int) -> bool
	pass

def callUpdater( *args, **kwargs ) :
	""" allow the game to update during startup """

def cardinalDirectionToDirection( arg0 ) :
	# type: (int) -> int
	""" converts a CardinalDirectionType to the corresponding DirectionType """

def cyFloatRange( arg0, arg1, arg2 ) :
	# type: (float, float, float) -> float
	pass

def cyIntRange( arg0, arg1, arg2 ) :
	# type: (int, int, int) -> int
	pass

def destroyWBDiplomacyCtrl( *args, **kwargs ) :
	""" void cyDestroyWBDiplomacyCtrl() - initializes the starting place for the world builder tab ctrls """

def directionXY( arg0, arg1 ) :
	# type: (int, int) -> int
	pass

def directionXYFromPlot( arg0, arg1 ) :
	# type: (CyPlot, CyPlot) -> int
	pass

def dxWrap( arg0 ) :
	# type: (int) -> int
	pass

def dyWrap( arg0 ) :
	# type: (int) -> int
	pass

def estimateDirection( arg0, arg1 ) :
	# type: (int, int) -> int
	pass

false = 0 # type: int

def finalImprovementUpgrade( arg0, arg1 ) :
	# type: (int, int) -> int
	pass

def getASBuilding( arg0 ) :
	# type: (int) -> Any
	pass

def getASImprovement( arg0 ) :
	# type: (int) -> Any
	pass

def getASRoute( arg0 ) :
	# type: (int) -> Any
	pass

def getASUnit( arg0 ) :
	# type: (int) -> Any
	pass

def getAlarmHour(  ) :
	# type: () -> int
	""" Returns the clock hour when the alarm is set to go off """

def getAlarmHourLeft(  ) :
	# type: () -> int
	""" Returns the number of hours left before the alarm is set to go off """

def getAlarmMin(  ) :
	# type: () -> int
	""" Returns the clock minute when the alarm is set to go off """

def getAlarmMinLeft(  ) :
	# type: () -> int
	""" Returns the number of minutes (excluding those accounted for by the hours) left before the alarm is set to go off """

def getChtLvl( *args, **kwargs ) :
	""" get cheat level """

def getCity( arg0 ) :
	# type: (IDInfo) -> CyPlot
	pass

def getClockText(  ) :
	# type: () -> unicode
	""" returns the string for the time (localized) """

def getCombatOdds( arg0, arg1 ) :
	# type: (CyUnit, CyUnit) -> int
	pass

def getCyDefinesVarSystem( *args, **kwargs ) :
	""" getCyDefinesVarSystem """

def getEra( *args, **kwargs ) :
	""" get game era index """

def getEspionageModifier( arg0, arg1 ) :
	# type: (int, int) -> int
	pass

def getExeLinkDate( iFromX, iToX ) :
	# type: (Any, Any) -> int
	pass

def getLandPlotsAsset( arg0 ) :
	# type: (int) -> int
	pass

def getLandPlotsScore( arg0 ) :
	# type: (int) -> int
	pass

def getModulePathName( *args, **kwargs ) :
	pass

def getOppositeCardinalDirection( arg0 ) :
	# type: (int) -> int
	pass

def getPopulationAsset( arg0 ) :
	# type: (int) -> int
	pass

def getPopulationPower( arg0 ) :
	# type: (int) -> int
	pass

def getPopulationScore( arg0 ) :
	# type: (int) -> int
	pass

def getSyncRandomSeed( *args, **kwargs ) :
	""" get game random seed """

def getTechScore( arg0 ) :
	# type: (int) -> int
	pass

def getUnit( arg0 ) :
	# type: (IDInfo) -> CyUnit
	pass

def getWBSaveExtension( *args, **kwargs ) :
	""" getWBSaveExtension """

def getWBSaveFolder( *args, **kwargs ) :
	""" getWBSaveFolder """

def getWBToolAdvancedStartTabCtrl(  ) :
	# type: () -> Any
	""" gets the worldbuilder tool normal player tab control """

def getWBToolDiplomacyTabCtrl(  ) :
	# type: () -> Any
	""" gets the worldbuilder tool diplomacy tab control """

def getWBToolEditTabCtrl(  ) :
	# type: () -> Any
	""" gets the worldbuilder tool edit tab control """

def getWBToolNormalMapTabCtrl(  ) :
	# type: () -> Any
	""" gets the worldbuilder tool normal map tab control """

def getWBToolNormalPlayerTabCtrl(  ) :
	# type: () -> Any
	""" gets the worldbuilder tool normal player tab control """

def getWonderScore( arg0 ) :
	# type: (int) -> int
	pass

def getWorldSizeMaxConscript( arg0 ) :
	# type: (int) -> int
	pass

def initWBDiplomacyCtrl( *args, **kwargs ) :
	""" void cyInitWBDiplomacyCtrl() - initializes the starting place for the world builder tab ctrls """

def initWBToolAdvancedStartControl(  ) :
	# type: () -> cyInitWBToolAdvancedStartControl
	""" inits the worldbuilder tool AdvancedStart control """

def initWBToolEditCtrl(  ) :
	# type: () -> cyInitWBToolEditCtrl
	""" inits the worldbuilder tool edit control """

def initWBToolEditCtrlTab( *args, **kwargs ) :
	""" void cyInitWBToolEditCtrlTab(bool bUnit) - inits the worldbuilder tool edit control's second tab, either promotions for a unit edit control or buildings for a city edit control """

def initWBToolPlayerControl(  ) :
	# type: () -> cyInitWBToolPlayerControl
	""" inits the worldbuilder tool player control """

def isAlarmOn(  ) :
	# type: () -> bool
	""" Returns whether or not the alarm is currently set """

def isCardinalDirection( arg0 ) :
	# type: (int) -> bool
	pass

def isLimitedProject( arg0 ) :
	# type: (int) -> bool
	pass

def isLimitedUnitClass( arg0 ) :
	# type: (int) -> bool
	pass

def isLimitedWonderClass( arg0 ) :
	# type: (int) -> bool
	pass

def isMouseOverGameSurface( *args, **kwargs ) :
	pass

def isNationalUnitClass( arg0 ) :
	# type: (int) -> bool
	pass

def isNationalWonderClass( arg0 ) :
	# type: (int) -> bool
	pass

def isPotentialEnemy( arg0, arg1 ) :
	# type: (int, int) -> bool
	pass

def isPromotionValid( arg0, arg1, arg2 ) :
	# type: (int, int, bool) -> bool
	pass

def isReligionTech( arg0 ) :
	# type: (int) -> int
	pass

def isTeamProject( arg0 ) :
	# type: (int) -> bool
	pass

def isTeamUnitClass( arg0 ) :
	# type: (int) -> bool
	pass

def isTeamWonderClass( arg0 ) :
	# type: (int) -> bool
	pass

def isTechRequiredForBuilding( arg0, arg1 ) :
	# type: (int, int) -> bool
	pass

def isTechRequiredForProject( arg0, arg1 ) :
	# type: (int, int) -> bool
	pass

def isTechRequiredForUnit( arg0, arg1 ) :
	# type: (int, int) -> bool
	pass

def isWorldProject( arg0 ) :
	# type: (int) -> bool
	pass

def isWorldUnitClass( arg0 ) :
	# type: (int) -> bool
	pass

def isWorldWonderClass( arg0 ) :
	# type: (int) -> bool
	pass

def loadImportModule( *args, **kwargs ) :
	pass

def plotCardinalDirection( arg0, arg1, arg2 ) :
	# type: (int, int, int) -> CyPlot
	pass

def plotCity( arg0, arg1, arg2 ) :
	# type: (int, int, int) -> CyPlot
	pass

def plotCityXY( arg0, arg1 ) :
	# type: (int, int) -> int
	pass

def plotCityXYFromCity( arg0, arg1 ) :
	# type: (CyCity, CyPlot) -> int
	pass

def plotDirection( arg0, arg1, arg2 ) :
	# type: (int, int, int) -> CyPlot
	pass

def plotDistance( arg0, arg1, arg2, arg3 ) :
	# type: (int, int, int, int) -> int
	pass

def plotXY( arg0, arg1, arg2, arg3 ) :
	# type: (int, int, int, int) -> CyPlot
	pass

def refreshWBEditCtrlCorporationButtons( *args, **kwargs ) :
	""" void cyRefreshWorldBuilder2EditControlCorporationButtons() - refreshes the corporation and headquarter buttons on the edit control tab """

def refreshWBEditCtrlReligionButtons( *args, **kwargs ) :
	""" void cyRefreshWorldBuilder2EditControlReligionButtons() - refreshes the religion and holy city buttons on the edit control tab """

def saveDiplomacySettings( *args, **kwargs ) :
	""" void cySaveDiplomacySettings() - initializes the starting place for the world builder tab ctrls """

def setAlarmHour( arg0 ) :
	# type: (int) -> None
	""" Sets the alarm to go off at iHour """

def setAlarmMin( arg0 ) :
	# type: (int) -> None
	""" Sets the alarm to go off at iHour """

def setDiplomacySettings( *args, **kwargs ) :
	""" void cySetDiplomacySettings() - initializes the starting place for the world builder tab ctrls """

def setFocusToCVG( *args, **kwargs ) :
	pass

def setHeights( arg0, arg1, arg2, arg3, arg4 ) :
	# type: (List, int, int, CyFractal, int) -> None
	pass

def setNoIntroMovie( *args, **kwargs ) :
	""" No intro """

def setWBInitialCtrlTabPlacement( *args, **kwargs ) :
	""" void cySetWBInitialCtrlTabPlacement() - initializes the starting place for the world builder tab ctrls """

def shuffleList( arg0, arg1, arg2 ) :
	# type: (int, CvRandom, List) -> None
	pass

def splotCardinalDirection( arg0, arg1, arg2 ) :
	# type: (int, int, int) -> CyPlot
	pass

def splotXY( arg0, arg1, arg2, arg3 ) :
	# type: (int, int, int, int) -> CyPlot
	pass

def stepDistance( arg0, arg1, arg2, arg3 ) :
	# type: (int, int, int, int) -> int
	pass

def toggleAlarm( arg0, arg1, arg2 ) :
	# type: (bool, int, int) -> None
	""" Turns on (or off) the alarm to go off in iHour and iMin """

true = 1 # type: int
