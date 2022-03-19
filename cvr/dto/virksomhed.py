from collections import defaultdict

from cvr.dto.utils import parse_date_time


def map_to_objects(dicts):
    return [Virksomhed(d) for d in dicts]


class Virksomhed:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.aarsbeskaeftigelse = [Aarsbeskaeftigelse(a) for a in obj.get("aarsbeskaeftigelse", [])]
        self.attributter = [Attribut(a) for a in obj.get("attributter", [])]
        self.beliggenhedsadresse = [Adresse(a) for a in obj.get("beliggenhedsadresse", [])]
        self.bibranche1 = [Branche(b) for b in obj.get("bibranche1", [])]
        self.bibranche2 = [Branche(b) for b in obj.get("bibranche2", [])]
        self.bibranche3 = [Branche(b) for b in obj.get("bibranche3", [])]
        self.branche_ansvarskode = obj.get("brancheAnsvarskode", None)
        self.cvr_nummer = obj.get("cvrNummer")
        self.data_adgang = obj.get("dataAdgang", None)
        self.deltager_relation = [DeltagerRelation(d) for d in obj.get("deltagerRelation", [])]
        self.elektronisk_post = [Kontaktoplysning(k) for k in obj.get("elektroniskPost", [])]
        self.enhedsnummer = obj.get("enhedsNummer", None)
        self.enhedstype = obj.get("enhedstype", None)
        self.fejl_beskrivelse = obj.get("fejlBeskrivelse", None)
        self.fejl_registreret = obj.get("fejlRegistreret", None)
        self.fejl_ved_indlaesning = obj.get("fejlVedIndlaesning", None)
        self.fusioner = [Fusion(f) for f in obj.get("fusioner", [])]
        self.hjemmeside = Kontaktoplysning(obj.get("hjemmeside", None))
        self.hovedbranche = [Branche(b) for b in obj.get("hovedbranche", [])]
        self.kvartalsbeskaeftigelse = [Kvartalsbeskaeftigelse(k) for k in obj.get("kvartalsbeskaeftigelse", [])]
        self.livsforloeb = [Livsforloeb(lf) for lf in obj.get("livsforloeb", [])]
        self.naermeste_fremtidige_dato = obj.get("naermesteFremtidigeDato", None)
        self.navne = [Navn(n) for n in obj.get("navne", [])]
        self.oblogatorisk_email = ObligatoriskEmail(obj.get("obligatoriskEmail", None))
        self.penheder = [Produktionsenhed(p) for p in obj.get("penheder", [])]
        self.postadresse = [Adresse(a) for a in obj.get("postadresse", [])]
        self.reg_nummer = [RegNummer(r) for r in obj.get("regNummer", None)]
        self.reklamebeskyttet = obj.get("reklamebeskyttet", None)
        self.samt_id = obj.get("samtId", None)
        self.sekundaert_telefax_nummer = Kontaktoplysning(obj.get("sekundaertTelefaxNummer", None))
        self.sekundaert_telefon_nummer = Kontaktoplysning(obj.get("sekundaertTelefonNummer", None))
        self.sidst_indlaest = parse_date_time(obj.get("sidstIndlaest", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))
        self.spaltninger = [Spaltning(s) for s in obj.get("spaltninger", [])]
        self.status = Status(obj.get("status", None))
        self.telefax_nummer = [Kontaktoplysning(k) for k in obj.get("telefaxNummer", [])]
        self.telefon_nummer = [Kontaktoplysning(k) for k in obj.get("telefonNummer", [])]
        self.virkningsaktoer = obj.get("virkningsAktoer", None)
        self.metadata = Metadata(obj.get("virksomhedMetadata", None))
        self.virksomhedsstatus = [Virksomhedsstatus(vs) for vs in obj.get("virksomhedsstatus", [])]


class Aarsbeskaeftigelse:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.aar = obj.get("aar", None)
        self.antal_aarsvaerk = obj.get("antalAarsvaerk", None)
        self.antal_ansatte = obj.get("antalAnsatte", None)
        self.antal_inklusiv_ejere = obj.get("antalInklusivEjere", None)
        self.interval_kode_antal_aarsvaerk = obj.get("intervalKodeAntalAarsvaerk", None)
        self.interval_kode_antal_ansatte = obj.get("intervalKodeAntalAnsatte", None)
        self.interval_kode_antal_inklusiv_ejere = obj.get("intervalKodeAntalInklusivEjere", None)
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Attribut:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.sekvensnr = obj.get("sekvensnr", None)
        self.type = obj.get("type", None)
        self.vaerditype = obj.get("vaerditype", None)
        self.vaerdier = [AttributVaerdi(a) for a in obj.get("vaerdier", None)]
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class AttributVaerdi:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.vaerdi = obj.get("vaerdi", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Periode:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.gyldig_fra = parse_date_time(obj.get("gyldigFra", None))
        self.gyldig_til = parse_date_time(obj.get("gyldigTil", None))


class Adresse:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.bogstav_fra = obj.get("bogstavFra", None)
        self.bogstav_til = obj.get("bogstavTil", None)
        self.bynavn = obj.get("bynavn", None)
        self.conavn = obj.get("conavn", None)
        self.etage = obj.get("etage", None)
        self.fritekst = obj.get("fritekst", None)
        self.husnummer_fra = obj.get("husnummerFra", None)
        self.adresse_id = obj.get("adresseId", None)
        self.husnummer_til = obj.get("husnummerTil", None)
        self.kommune = Kommune(obj.get("kommune", {}))
        self.landekode = obj.get("landekode", None)
        self.periode = Periode(obj.get("periode", None))
        self.postboks = obj.get("postboks", None)
        self.postdistrikt = obj.get("postdistrikt", None)
        self.postnummer = obj.get("postnummer", None)
        self.sidedoer = obj.get("sidedoer", None)
        self.sidst_valideret = obj.get("sidstValideret", None)
        self.vejkode = obj.get("vejkode", None)
        self.vejnavn = obj.get("vejnavn", None)
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Branche:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.branchekode = obj.get("branchekode", None)
        self.branchetekst = obj.get("branchetekst", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class DeltagerRelation:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Kontaktoplysning:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.hemmelig = obj.get("hemmelig", None)
        self.kontaktoplysning = obj.get("kontaktoplysning", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Kvartalsbeskaeftigelse:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.aar = obj.get("aar", None)
        self.kvartal = obj.get("kvartal", None)
        self.antal_aarsvaerk = obj.get("antalAarsvaerk", None)
        self.antal_ansatte = obj.get("antalAnsatte", None)
        self.antal_inklusiv_ejere = obj.get("antalInklusivEjere", None)
        self.interval_kode_antal_aarsvaerk = obj.get("intervalKodeAntalAarsvaerk", None)
        self.interval_kode_antal_ansatte = obj.get("intervalKodeAntalAnsatte", None)
        self.interval_kode_antal_inklusiv_ejere = obj.get("intervalKodeAntalInklusivEjere", None)
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Kommune:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.kommune_kode = obj.get("kommuneKode", None)
        self.kommune_navn = obj.get("kommuneNavn", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Livsforloeb:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Navn:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.navn = obj.get("navn", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Virksomhedsrelation:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.cvr_nummer = obj.get("cvrNummer", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Fusion:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.enheds_nummer_organisation = obj.get("enhedsNummerOrganisation", None)
        self.organisations_navn = [Navn(n) for n in obj.get("organisationsNavn", [])]
        self.indgaaende = [Attribut(a) for a in obj.get("indgaaende", [])]
        self.udgaaende = [Attribut(a) for a in obj.get("udgaaende", [])]


class Spaltning:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.enheds_nummer_organisation = obj.get("enhedsNummerOrganisation", None)
        self.organisations_navn = [Navn(n) for n in obj.get("organisationsNavn", [])]
        self.indgaaende = [Attribut(a) for a in obj.get("indgaaende", [])]
        self.udgaaende = [Attribut(a) for a in obj.get("udgaaende", [])]


class Metadata:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.nyeste_navn = Navn(obj.get("nyesteNavn", None))
        self.nyeste_binavne = obj.get("nyesteBinavne", [])
        self.nyeste_virksomhedsform = Virksomhedsform(obj.get("nyesteVirksomhedsform", None))
        self.nyeste_beliggenhedsadresse = Adresse(obj.get("nyesteBeliggenhedsadresse", None))
        self.nyeste_hovedbranche = Branche(obj.get("nyesteHovedbranche", None))
        self.nyeste_bibranche1 = obj.get("nyesteBibranche1", None)
        self.nyeste_bibranche2 = obj.get("nyesteBibranche2", None)
        self.nyeste_bibranche3 = obj.get("nyesteBibranche3", None)
        self.nyeste_status = obj.get("nyesteStatus", None)
        self.nyeste_kontaktoplysninger = obj.get("nyesteKontaktoplysninger", None)
        self.antal_penheder = obj.get("antalPenheder", None)
        self.nyeste_aarsbeskaeftigelse = obj.get("nyesteAarsbeskaeftigelse", None)
        self.nyeste_kvartalsbeskaeftigelse = obj.get("nyesteKvartalsbeskaeftigelse", None)
        self.nyeste_maanedsbeskaeftigelse = obj.get("nyesteMaanedsbeskaeftigelse", None)
        self.sammensat_status = obj.get("sammensatStatus", None)
        self.stiftelses_dato = obj.get("stiftelsesDato", None)
        self.virknings_dato = obj.get("virkningsDato", None)


class Produktionsenhed:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.p_nummer = obj.get("pNummer", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Status:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.kreditoplysningskode = obj.get("kreditoplysningskode", None)
        self.kreditoplysningstekst = obj.get("kreditoplysningstekst", None)
        self.statuskode = obj.get("statuskode", None)
        self.statustekst = obj.get("statustekst", None)
        self.periode = obj.get("periode", None)


class Virksomhedsstatus:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.status = obj.get("status", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class RegNummer:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.reg_nummer = obj.get("regnummer", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class ObligatoriskEmail:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.hemmelig = obj.get("hemmelig", None)
        self.kontaktoplysning = obj.get("kontaktoplysning", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))


class Virksomhedsform:
    def __init__(self, obj):
        obj = obj or defaultdict(lambda: None)
        self.ansvarlig_dataleverandoer = obj.get("ansvarligDataleverandoer", None)
        self.kort_beskrivelse = obj.get("kortBeskrivelse", None)
        self.lang_beskrivelse = obj.get("langBeskrivelse", None)
        self.periode = Periode(obj.get("periode", None))
        self.sidst_opdateret = parse_date_time(obj.get("sidstOpdateret", None))
