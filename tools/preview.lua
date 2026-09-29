-- Prints sample names from the mod's name script, without the game.
--
--   lua tools/preview.lua            10 of each
--   lua tools/preview.lua 25         25 of each
--   lua tools/preview.lua 25 42      25 of each, seed 42 (same output every run)

local count = tonumber(arg[1]) or 10
local seed = tonumber(arg[2])
if seed then
  math.randomseed(seed)
end

local root = arg[0]:match("^(.*)/tools/[^/]*$") or "."

-- The game resolves require "x.lua" next to the requiring script;
-- plain Lua does not, so map those names to content/names/ here.
table.insert(package.searchers, 2, function(name)
  if name:match("%.lua$") then
    local path = root .. "/hertzg_georgian_names/content/names/" .. name
    return assert(loadfile(path)), path
  end
end)

dofile(root .. "/hertzg_georgian_names/content/names/georgian.script.lua")
local fns = data()

local function section(title, names)
  print("== " .. title)
  for _, name in ipairs(names) do
    print("  " .. name)
  end
  print()
end

local function people(isMale)
  local names = {}
  for i = 1, count do
    names[i] = fns.personNameScriptFn(nil, { isMale = isMale })
  end
  return names
end

section("men", people(true))
section("women", people(false))
section("towns", fns.townsNameScriptFn(nil, { num = count }))
section("streets", fns.streetsNameScriptFn(nil, { num = count }))
