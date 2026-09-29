-- Georgian name lists. Each entry is { latin, georgian }.
-- captureParams.script picks the column: "latin" -> 1, "georgian" -> 2.

-- First names are in the form used before a surname,
-- so the nominative -ი is dropped (დავითი -> დავით ბერიძე).
local maleFirstNames = {
  { "Giorgi", "გიორგი" }, { "Davit", "დავით" }, { "Luka", "ლუკა" },
  { "Nikoloz", "ნიკოლოზ" }, { "Irakli", "ირაკლი" }, { "Levan", "ლევან" },
  { "Zurab", "ზურაბ" }, { "Giga", "გიგა" }, { "Tornike", "ტორნიკე" },
  { "Lasha", "ლაშა" }, { "Nika", "ნიკა" }, { "Aleksandre", "ალექსანდრე" },
  { "Vakhtang", "ვახტანგ" }, { "Tamaz", "თამაზ" }, { "Revaz", "რევაზ" },
  { "Shota", "შოთა" }, { "Otar", "ოთარ" }, { "Beka", "ბექა" },
  { "Gela", "გელა" }, { "Mamuka", "მამუკა" }, { "Temur", "თემურ" },
  { "Archil", "არჩილ" }, { "Dachi", "დაჩი" }, { "Saba", "საბა" },
}

local femaleFirstNames = {
  { "Nino", "ნინო" }, { "Mariam", "მარიამ" }, { "Tamar", "თამარ" },
  { "Ana", "ანა" }, { "Elene", "ელენე" }, { "Salome", "სალომე" },
  { "Natia", "ნატია" }, { "Ketevan", "ქეთევან" }, { "Nana", "ნანა" },
  { "Maia", "მაია" }, { "Eka", "ეკა" }, { "Tamta", "თამთა" },
  { "Sopio", "სოფიო" }, { "Lika", "ლიკა" }, { "Nutsa", "ნუცა" },
  { "Teona", "თეონა" }, { "Khatia", "ხატია" }, { "Lela", "ლელა" },
  { "Manana", "მანანა" }, { "Tinatin", "თინათინ" }, { "Medea", "მედეა" },
  { "Rusudan", "რუსუდან" }, { "Keti", "ქეთი" }, { "Irma", "ირმა" },
}

-- Georgian surnames are the same for men and women.
local surnames = {
  { "Beridze", "ბერიძე" }, { "Kapanadze", "კაპანაძე" }, { "Gelashvili", "გელაშვილი" },
  { "Maisuradze", "მაისურაძე" }, { "Giorgadze", "გიორგაძე" }, { "Lomidze", "ლომიძე" },
  { "Tsiklauri", "წიკლაური" }, { "Bolkvadze", "ბოლქვაძე" }, { "Kvaratskhelia", "კვარაცხელია" },
  { "Nozadze", "ნოზაძე" }, { "Abashidze", "აბაშიძე" }, { "Khutsishvili", "ხუციშვილი" },
  { "Mikeladze", "მიქელაძე" }, { "Tabatadze", "ტაბატაძე" }, { "Chkheidze", "ჩხეიძე" },
  { "Kiknadze", "კიკნაძე" }, { "Janelidze", "ჯანელიძე" }, { "Dolidze", "დოლიძე" },
  { "Javakhishvili", "ჯავახიშვილი" }, { "Chikovani", "ჩიქოვანი" }, { "Shengelia", "შენგელია" },
  { "Todua", "თოდუა" }, { "Gabunia", "გაბუნია" }, { "Kharebava", "ხარებავა" },
  { "Chanturia", "ჭანტურია" }, { "Metreveli", "მეტრეველი" }, { "Tsereteli", "წერეთელი" },
  { "Natroshvili", "ნატროშვილი" }, { "Svanidze", "სვანიძე" }, { "Makharadze", "მახარაძე" },
}

local towns = {
  { "Tbilisi", "თბილისი" }, { "Kutaisi", "ქუთაისი" }, { "Batumi", "ბათუმი" },
  { "Rustavi", "რუსთავი" }, { "Zugdidi", "ზუგდიდი" }, { "Gori", "გორი" },
  { "Poti", "ფოთი" }, { "Zestaponi", "ზესტაფონი" }, { "Khashuri", "ხაშური" },
  { "Samtredia", "სამტრედია" }, { "Senaki", "სენაკი" }, { "Telavi", "თელავი" },
  { "Akhaltsikhe", "ახალციხე" }, { "Kobuleti", "ქობულეთი" }, { "Ozurgeti", "ოზურგეთი" },
  { "Kaspi", "კასპი" }, { "Chiatura", "ჭიათურა" }, { "Tskaltubo", "წყალტუბო" },
  { "Sagarejo", "საგარეჯო" }, { "Gardabani", "გარდაბანი" }, { "Borjomi", "ბორჯომი" },
  { "Tkibuli", "ტყიბული" }, { "Khoni", "ხონი" }, { "Bolnisi", "ბოლნისი" },
  { "Akhalkalaki", "ახალქალაქი" }, { "Gurjaani", "გურჯაანი" }, { "Mtskheta", "მცხეთა" },
  { "Kvareli", "ყვარელი" }, { "Akhmeta", "ახმეტა" }, { "Kareli", "ქარელი" },
  { "Lanchkhuti", "ლანჩხუთი" }, { "Tsalenjikha", "წალენჯიხა" }, { "Dusheti", "დუშეთი" },
  { "Sachkhere", "საჩხერე" }, { "Dedoplistskaro", "დედოფლისწყარო" }, { "Lagodekhi", "ლაგოდეხი" },
  { "Ninotsminda", "ნინოწმინდა" }, { "Abasha", "აბაშა" }, { "Tsnori", "წნორი" },
  { "Terjola", "თერჯოლა" }, { "Martvili", "მარტვილი" }, { "Khobi", "ხობი" },
  { "Vani", "ვანი" }, { "Baghdati", "ბაღდათი" }, { "Vale", "ვალე" },
  { "Tetritskaro", "თეთრიწყარო" }, { "Tsalka", "წალკა" }, { "Dmanisi", "დმანისი" },
  { "Oni", "ონი" }, { "Ambrolauri", "ამბროლაური" }, { "Sighnaghi", "სიღნაღი" },
  { "Mestia", "მესტია" }, { "Pasanauri", "ფასანაური" }, { "Stepantsminda", "სტეფანწმინდა" },
  { "Bakuriani", "ბაკურიანი" }, { "Gudauri", "გუდაური" }, { "Bulachauri", "ბულაჩაური" },
}

-- Extra towns beyond the list get a real Georgian prefix: Upper / Lower.
local townPrefixes = {
  { "Zemo ", "ზემო " }, { "Kvemo ", "ქვემო " },
}

-- Street name bases. The Georgian column is already in the genitive case,
-- which is how streets are named (რუსთაველის ქუჩა = Rustaveli Street).
local streetBases = {
  { "Rustaveli", "რუსთაველის" }, { "Chavchavadze", "ჭავჭავაძის" },
  { "Kazbegi", "ყაზბეგის" }, { "Tsereteli", "წერეთლის" },
  { "Vazha-Pshavela", "ვაჟა-ფშაველას" }, { "Aghmashenebeli", "აღმაშენებლის" },
  { "Kostava", "კოსტავას" }, { "Tamar Mepe", "თამარ მეფის" },
  { "Paliashvili", "ფალიაშვილის" }, { "Javakhishvili", "ჯავახიშვილის" },
  { "Barnovi", "ბარნოვის" }, { "Gamsakhurdia", "გამსახურდიას" },
  { "Machabeli", "მაჩაბლის" }, { "Tabidze", "ტაბიძის" },
  { "Gorgasali", "გორგასლის" }, { "Marjanishvili", "მარჯანიშვილის" },
  { "Pirosmani", "ფიროსმანის" }, { "Baratashvili", "ბარათაშვილის" },
  { "Leonidze", "ლეონიძის" }, { "Abashidze", "აბაშიძის" },
  { "Station", "სადგურის" }, { "Railway", "რკინიგზის" },
}

local streetTypes = {
  { "Street", "ქუჩა" }, { "Avenue", "გამზირი" }, { "Lane", "შესახვევი" },
}

local function column(captureParams)
  if captureParams.script == "georgian" then
    return 2
  end
  return 1
end

local function pick(list, col)
  return list[math.random(#list)][col]
end

local function shuffle(list)
  for i = #list, 2, -1 do
    local j = math.random(i)
    list[i], list[j] = list[j], list[i]
  end
  return list
end

-- Takes `num` names in random order, using up `main` before touching `extra`.
-- num = -1 means all.
local function take(main, extra, num)
  local names = shuffle(main)
  for _, name in ipairs(shuffle(extra)) do
    names[#names + 1] = name
  end
  if num == -1 then
    return names
  end
  local result = {}
  for i = 1, math.min(num, #names) do
    result[#result + 1] = names[i]
  end
  return result
end

local function townNames(col, num)
  local main, extra = {}, {}
  for _, town in ipairs(towns) do
    main[#main + 1] = town[col]
    for _, prefix in ipairs(townPrefixes) do
      extra[#extra + 1] = prefix[col] .. town[col]
    end
  end
  return take(main, extra, num)
end

-- Latin: "Rustaveli Street", Georgian: "რუსთაველის ქუჩა".
-- Extra: numbered lanes the Georgian way, "რუსთაველის მე-2 შესახვევი".
local function streetNames(col, num)
  local main, extra = {}, {}
  for _, base in ipairs(streetBases) do
    for _, streetType in ipairs(streetTypes) do
      main[#main + 1] = base[col] .. " " .. streetType[col]
    end
    for n = 2, 5 do
      if col == 2 then
        extra[#extra + 1] = base[col] .. " მე-" .. n .. " შესახვევი"
      else
        extra[#extra + 1] = base[col] .. " Lane " .. n
      end
    end
  end
  return take(main, extra, num)
end

function data()
return {
  personNameScriptFn = function(captureParams, params)
    local col = column(captureParams)
    local firstNames = params.isMale and maleFirstNames or femaleFirstNames
    return pick(firstNames, col) .. " " .. pick(surnames, col)
  end,

  townsNameScriptFn = function(captureParams, params)
    return townNames(column(captureParams), params.num)
  end,

  streetsNameScriptFn = function(captureParams, params)
    return streetNames(column(captureParams), params.num)
  end,
}
end
