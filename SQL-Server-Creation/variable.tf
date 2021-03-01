variable "db_name" {
  type = string
}

variable "rg_name" {
  type = string
}

variable "location" {
  type = string
}

# The sensitive = true configuration ensures no accidentally exposed secrets in CLI output, log output, or source control   
variable "password" {
  type = string
  sensitive = true
}

variable "ip_address" {
  type = string
  sensitive = true
}