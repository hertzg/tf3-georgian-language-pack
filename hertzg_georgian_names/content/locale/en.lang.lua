-- Adds "English + Georgian" to Settings > Language: the base game's English
-- with Georgian Names Sans as the UI font (the game's Lato plus Georgian
-- letters), so Georgian names can be drawn. Mods add languages; they can't
-- change the base ones. The game loads every font listed here from this
-- mod's locale folder, and the language's text from this mod's strings folder.
function data()
return {
	name = "English + Georgian",
	locale = "en_US",
	fontMap = {
		regular = "GeorgianNamesSans/GeorgianNamesSans-Regular.ttf",
		bold = "GeorgianNamesSans/GeorgianNamesSans-Bold.ttf",
		light = "GeorgianNamesSans/GeorgianNamesSans-Light.ttf",
		medium = "GeorgianNamesSans/GeorgianNamesSans-Medium.ttf",
		monoRegular = "Noto/NotoSansMono-Regular.ttf",
		monoBold = "Noto/NotoSansMono-Bold.ttf",
	},
	unicodeFontMap = {
		regular = "GeorgianNamesSans/GeorgianNamesSans-Regular.ttf",
		bold = "GeorgianNamesSans/GeorgianNamesSans-Bold.ttf",
		monoRegular = "Noto/NotoSansMono-Regular.ttf",
		monoBold = "Noto/NotoSansMono-Bold.ttf",
		scaling = 1.0,
	},
}
end
